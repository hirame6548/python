import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def preformatted_math_to_markdown(pre: Tag) -> str:
    """入力形式の <pre><var>...</var></pre> を左寄せの数式行にする。"""
    lines: list[list[str]] = [[]]
    for child in pre.children:
        if isinstance(child, Tag):
            value = child.get_text().strip()
            if value:
                lines[-1].append(value)
            continue

        parts = str(child).split("\n")
        for index, part in enumerate(parts):
            value = part.strip()
            if value:
                lines[-1].append(r"\text{" + value.replace("}", r"\}") + "}")
            if index < len(parts) - 1:
                lines.append([])

    equations = ["$" + r" \quad ".join(line) + "$" for line in lines if line]
    return "\n" + "<br>\n".join(equations) + "\n"


def statement_to_markdown(html: str, url: str) -> str:
    """AtCoderのHTMLから日本語の問題文を読みやすいMarkdownへ変換する。"""
    soup = BeautifulSoup(html, "lxml")
    statement = soup.select_one("#task-statement")
    if statement is None:
        raise ValueError("問題文の領域 (#task-statement) が見つかりません")

    content = statement.select_one(".lang-ja") or statement
    for tag in content.select("script, style"):
        tag.decompose()

    for image in content.find_all("img"):
        src = image.get("src")
        if src:
            alt = image.get("alt", "問題文中の画像")
            image.replace_with(NavigableString(f"![{alt}]({urljoin(url, src)})"))

    for pre in content.find_all("pre"):
        if pre.find("var"):
            rendered = preformatted_math_to_markdown(pre)
        else:
            code = pre.get_text().strip("\n")
            rendered = f"\n```text\n{code}\n```\n"
        pre.replace_with(NavigableString(rendered))

    # AtCoderは数式を <var>...</var> に入れ、ブラウザ側でMathJax描画する。
    # MarkdownでもLaTeXとして認識できるようインライン数式に変換する。
    for math in content.find_all("var"):
        tex = math.get_text().strip()
        math.replace_with(NavigableString(f"${tex}$"))

    for table in content.find_all("table"):
        rows = []
        for row in table.find_all("tr"):
            cells = [
                cell.get_text(" ", strip=True).replace("|", r"\|")
                for cell in row.find_all(["th", "td"], recursive=False)
            ]
            if cells:
                rows.append(cells)
        if rows:
            width = max(map(len, rows))
            rows = [row + [""] * (width - len(row)) for row in rows]
            markdown_rows = ["| " + " | ".join(row) + " |" for row in rows]
            markdown_rows.insert(1, "| " + " | ".join(["---"] * width) + " |")
            table.replace_with(NavigableString("\n" + "\n".join(markdown_rows) + "\n"))

    for link in content.find_all("a"):
        label = link.get_text(strip=True)
        href = link.get("href")
        if label and href and not href.startswith("#"):
            link.replace_with(NavigableString(f"[{label}]({urljoin(url, href)})"))

    for heading in content.find_all(["h1", "h2", "h3", "h4"]):
        level = max(2, int(heading.name[1]) - 1)
        heading.insert_before(NavigableString(f"\n{'#' * level} "))
        heading.append(NavigableString("\n"))

    for item in content.find_all("li"):
        marker = "1." if item.parent and item.parent.name == "ol" else "-"
        item.insert_before(NavigableString(f"\n{marker} "))
        item.append(NavigableString("\n"))

    for br in content.find_all("br"):
        br.replace_with(NavigableString("\n"))

    for block in content.find_all(["p", "div", "section", "ul", "ol", "table", "tr"]):
        block.insert_before(NavigableString("\n"))
        block.append(NavigableString("\n"))

    lines = [line.rstrip() for line in content.get_text().splitlines()]
    body = "\n".join(lines).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return f"# 問題文\n\n出典: {url}\n\n{body}\n"


def download_statement(url: str, destination: Path) -> None:
    response = requests.get(
        url,
        headers={"User-Agent": "atcoder-template/1.0"},
        timeout=30,
    )
    response.raise_for_status()
    destination.write_text(
        statement_to_markdown(response.text, url),
        encoding="utf-8",
    )


def normalize_contest_id(value: str) -> str:
    return value.strip().lower().replace("-", "_")


def infer_contest_id(contest_root: Path) -> str | None:
    """新旧どちらのフォルダ構造からもコンテストIDを推測する。"""
    config_file = contest_root / "contest.json"
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text(encoding="utf-8"))
            contest_id = config.get("contest_id")
        except (OSError, json.JSONDecodeError):
            contest_id = None
        if isinstance(contest_id, str) and contest_id:
            return normalize_contest_id(contest_id)

    category = contest_root.parent.name.lower()
    if category in {"abc", "arc", "agc", "ahc", "awc"}:
        return f"{category}{contest_root.name.lower()}"

    if (
        contest_root.parent.parent.name.lower() == "adt"
        and contest_root.parent.name.lower() in {"easy", "all"}
    ):
        course = contest_root.parent.name.lower()
        return f"adt_{course}_{contest_root.name.lower()}"

    normalized = re.sub(r"[_-]", "", contest_root.name.lower())

    short_name = re.search(r"(abc|arc|agc|ahc|awc)\d+", normalized)
    if short_name:
        return short_name.group()

    long_names = {
        "atcoderbeginnercontest": "abc",
        "atcoderregularcontest": "arc",
        "atcodergrandcontest": "agc",
    }
    for prefix, abbreviation in long_names.items():
        match = re.search(rf"{prefix}(\d+)", normalized)
        if match:
            return f"{abbreviation}{match.group(1)}"

    return None


def parse_tasks(html: str, contest_id: str) -> dict[str, str]:
    tasks_url = f"https://atcoder.jp/contests/{contest_id}/tasks"
    soup = BeautifulSoup(html, "lxml")
    tasks: dict[str, str] = {}
    for row in soup.select("table tbody tr"):
        cells = row.find_all("td", recursive=False)
        if not cells:
            continue
        link = row.select_one(f'a[href^="/contests/{contest_id}/tasks/"]')
        if link is None or not link.get("href"):
            continue
        label = cells[0].get_text(" ", strip=True).upper()
        if label:
            tasks[label] = urljoin(tasks_url, str(link["href"]))

    return tasks


def discover_tasks(contest_id: str) -> dict[str, str]:
    """タスク一覧から表示ラベルと実際の問題URLを取得する。"""
    tasks_url = f"https://atcoder.jp/contests/{contest_id}/tasks"
    response = requests.get(
        tasks_url,
        headers={"User-Agent": "atcoder-template/1.0"},
        timeout=30,
    )
    response.raise_for_status()
    tasks = parse_tasks(response.text, contest_id)
    if not tasks:
        raise ValueError(
            "問題一覧を取得できませんでした。コンテスト開始前、"
            "またはコンテストIDが違う可能性があります。"
        )
    return tasks


def main(contest_root: Path | None = None) -> int:
    contest_root = (contest_root or Path.cwd()).resolve()
    parser = argparse.ArgumentParser(
        description="AtCoderの問題文と公式サンプルを各問題フォルダへ取得します。",
    )
    parser.add_argument(
        "contest_id",
        nargs="?",
        help="通常は省略できます。明示する場合の例: abc468",
    )
    parser.add_argument(
        "--labels",
        nargs="+",
        help="取得する問題ラベル（省略時は公式の問題一覧から判定）",
    )
    parser.add_argument(
        "--refresh-statements",
        action="store_true",
        help="取得済みのproblem.mdも最新の内容で上書きする",
    )
    args = parser.parse_args()

    oj = shutil.which("oj")
    if oj is None:
        parser.error("ojが見つかりません。online-judge-toolsをインストールしてください。")

    if args.contest_id:
        contest_id = normalize_contest_id(args.contest_id)
    else:
        contest_id = infer_contest_id(contest_root)
        if contest_id is None:
            parser.error(
                f"フォルダ {contest_root} からコンテストIDを判定できません。"
                "contest.jsonを確認してください。"
            )

    print(f"[contest] {contest_id}")
    try:
        tasks = discover_tasks(contest_id)
    except (requests.RequestException, ValueError) as error:
        parser.error(str(error))

    selected_labels = (
        [label.upper() for label in args.labels] if args.labels else list(tasks)
    )
    failed: set[str] = set()

    for label in selected_labels:
        url = tasks.get(label)
        if url is None:
            print(f"[skip] {label}: 公式の問題一覧にありません")
            continue

        task_dir = contest_root / label
        if not task_dir.is_dir():
            print(f"[skip] {label}: フォルダがありません")
            continue

        test_dir = task_dir / "test"
        test_dir.mkdir(exist_ok=True)
        if any(test_dir.glob("sample-*.in")):
            print(f"[skip] {label}: 公式サンプルを取得済みです")
        else:
            print(f"[download] {label}: {url}")

            result = subprocess.run(
                [oj, "download", url, "--directory", "test"],
                cwd=task_dir,
            )
            if result.returncode != 0:
                failed.add(label)
                continue

        statement_file = task_dir / "problem.md"
        if statement_file.exists() and not args.refresh_statements:
            print(f"[skip] {label}: 問題文を取得済みです")
        else:
            try:
                download_statement(url, statement_file)
            except (OSError, requests.RequestException, ValueError) as error:
                print(f"[error] {label}: 問題文を取得できませんでした: {error}")
                failed.add(label)
            else:
                print(f"[save] {label}: problem.md")

        sample_inputs = sorted(test_dir.glob("sample-*.in"))
        if not sample_inputs:
            print(f"[error] {label}: 入力例が見つかりません")
            failed.add(label)
            continue

        shutil.copyfile(sample_inputs[0], task_dir / "input.txt")
        print(f"[copy] {label}: {sample_inputs[0].name} → input.txt")

    if failed:
        print(f"取得に失敗しました: {', '.join(sorted(failed))}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
