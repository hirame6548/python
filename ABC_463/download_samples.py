import argparse
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).parent


def normalize_contest_id(value: str) -> str:
    return value.lower().replace("_", "").replace("-", "")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AtCoderの公式サンプルを各問題のtest/へ取得します。",
    )
    parser.add_argument("contest_id", help="例: abc467 または ABC_467")
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

    contest_id = normalize_contest_id(args.contest_id)
    failed = []

    for raw_label in args.labels:
        label = raw_label.upper()
        task_dir = ROOT / label
        if not task_dir.is_dir():
            print(f"[skip] {label}: フォルダがありません")
            continue

        test_dir = task_dir / "test"
        if any(test_dir.glob("sample-*.in")):
            print(f"[skip] {label}: 公式サンプルを取得済みです")
        else:
            problem_id = f"{contest_id}_{label.lower()}"
            url = f"https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}"
            print(f"[download] {label}: {url}")

            result = subprocess.run(
                [oj, "download", url, "--directory", "test"],
                cwd=task_dir,
            )
            if result.returncode != 0:
                failed.append(label)
                continue

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
