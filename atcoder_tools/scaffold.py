import argparse
import json
import re
import shutil
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = Path(__file__).resolve().parent / "template"

LABELS_BY_KIND = {
    "abc": list("ABCDEFG"),
    "arc": list("ABCDEF"),
    "agc": list("ABCDEF"),
    "ahc": ["A"],
    "awc": list("ABCDE"),
    "adt_easy": list("ABCDE"),
    "adt_all": list("ABCDEFGHI"),
}


def normalize_input(parts: list[str]) -> str:
    if len(parts) == 1:
        return parts[0].strip().lower().replace("-", "_")

    category = parts[0].strip().lower()
    if len(parts) == 2 and category in {"abc", "arc", "agc", "ahc", "awc"}:
        return category + parts[1].strip().lower()

    return "_".join(part.strip().lower() for part in parts)


def contest_spec(contest_id: str) -> tuple[Path, list[str]]:
    standard = re.fullmatch(r"(abc|arc|agc|ahc|awc)(\d+)", contest_id)
    if standard:
        kind, number = standard.groups()
        return Path(kind.upper()) / number, LABELS_BY_KIND[kind]

    adt = re.fullmatch(r"adt_(easy|all)_(\d{8})_(\d+)", contest_id)
    if adt:
        course, date, session = adt.groups()
        return (
            Path("ADT") / course.upper() / f"{date}_{session}",
            LABELS_BY_KIND[f"adt_{course}"],
        )

    raise ValueError(
        "コンテストIDの形式を認識できません。"
        "例: abc468, arc219, awc0141, adt_all_20260827_1"
    )


def create_contest(
    contest_id: str,
    labels: list[str] | None = None,
    repository_root: Path = REPOSITORY_ROOT,
) -> Path:
    relative_path, default_labels = contest_spec(contest_id)
    selected_labels = [label.upper() for label in (labels or default_labels)]
    destination = repository_root / relative_path

    if destination.exists():
        raise FileExistsError(f"すでに存在します: {destination}")

    destination.mkdir(parents=True)
    shutil.copy2(TEMPLATE_ROOT / "dl.py", destination / "dl.py")
    shutil.copy2(TEMPLATE_ROOT / "pytest.ini", destination / "pytest.ini")
    shutil.copytree(TEMPLATE_ROOT / ".vscode", destination / ".vscode")
    (destination / "contest.json").write_text(
        json.dumps(
            {"contest_id": contest_id, "labels": selected_labels},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    for label in selected_labels:
        task_dir = destination / label
        (task_dir / "test").mkdir(parents=True)
        shutil.copy2(TEMPLATE_ROOT / "main.py", task_dir / "main.py")
        shutil.copy2(TEMPLATE_ROOT / "test_main.py", task_dir / "test_main.py")
        shutil.copy2(TEMPLATE_ROOT / "test" / ".gitkeep", task_dir / "test" / ".gitkeep")

    return destination


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AtCoderコンテスト用フォルダを開始前に作成します。",
    )
    parser.add_argument(
        "contest",
        nargs="+",
        help="例: abc468（ABC 468のように分けても指定可能）",
    )
    parser.add_argument(
        "--labels",
        nargs="+",
        help="標準構成と異なる場合の問題ラベル。例: --labels A B C",
    )
    args = parser.parse_args()

    contest_id = normalize_input(args.contest)
    try:
        destination = create_contest(contest_id, args.labels)
    except (ValueError, FileExistsError) as error:
        parser.error(str(error))

    print(f"作成しました: {destination.relative_to(REPOSITORY_ROOT)}")
    print(f"VS Codeで開き、開始後に `python dl.py` を実行してください。")
    return 0
