import argparse
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString


ROOT = Path(__file__).resolve().parent


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
        code = pre.get_text().strip("\n")
        pre.replace_with(NavigableString(f"\n```text\n{code}\n```\n"))

    for heading in content.find_all(["h1", "h2", "h3", "h4"]):
        level = max(2, int(heading.name[1]) - 1)
        heading.insert_before(NavigableString(f"\n{'#' * level} "))
        heading.append(NavigableString("\n"))

    for item in content.find_all("li"):
        item.insert_before(NavigableString("\n- "))
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
    return value.lower().replace("_", "").replace("-", "")


def infer_contest_id(dirname: str) -> str | None:
    normalized = normalize_contest_id(dirname)

    short_name = re.search(r"(abc|arc|agc)\d+", normalized)
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


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AtCoderの問題文と公式サンプルを各問題フォルダへ取得します。",
    )
    parser.add_argument(
        "contest_id",
        nargs="?",
        help="省略時はフォルダ名から判定。例: abc467 または ABC_467",
    )
    parser.add_argument(
        "--labels",
        nargs="+",
        default=list("ABCDEFG"),
        help="取得する問題ラベル（デフォルト: A B C D E F G）",
    )
    args = parser.parse_args()

    oj = shutil.which("oj")
    if oj is None:
        parser.error("ojが見つかりません。online-judge-toolsをインストールしてください。")

    if args.contest_id:
        contest_id = normalize_contest_id(args.contest_id)
    else:
        contest_id = infer_contest_id(ROOT.name)
        if contest_id is None:
            parser.error(
                f"フォルダ名 {ROOT.name!r} からコンテストIDを判定できません。"
                "例: python dl.py abc467"
            )

    print(f"[contest] {contest_id}")
    failed = []

    for raw_label in args.labels:
        label = raw_label.upper()
        task_dir = ROOT / label
        if not task_dir.is_dir():
            print(f"[skip] {label}: フォルダがありません")
            continue

        problem_id = f"{contest_id}_{label.lower()}"
        url = f"https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}"
        test_dir = task_dir / "test"
        if any(test_dir.glob("sample-*.in")):
            print(f"[skip] {label}: 公式サンプルを取得済みです")
        else:
            print(f"[download] {label}: {url}")

            result = subprocess.run(
                [oj, "download", url, "--directory", "test"],
                cwd=task_dir,
            )
            if result.returncode != 0:
                failed.append(label)
                continue

        statement_file = task_dir / "problem.md"
        if statement_file.exists():
            print(f"[skip] {label}: 問題文を取得済みです")
        else:
            try:
                download_statement(url, statement_file)
            except (OSError, requests.RequestException, ValueError) as error:
                print(f"[error] {label}: 問題文を取得できませんでした: {error}")
                failed.append(label)
            else:
                print(f"[save] {label}: problem.md")

        sample_inputs = sorted(test_dir.glob("sample-*.in"))
        if not sample_inputs:
            print(f"[error] {label}: 入力例が見つかりません")
            failed.append(label)
            continue

        shutil.copyfile(sample_inputs[0], task_dir / "input.txt")
        print(f"[copy] {label}: {sample_inputs[0].name} → input.txt")

    if failed:
        print(f"取得に失敗しました: {', '.join(failed)}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
