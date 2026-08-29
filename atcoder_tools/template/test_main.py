import subprocess
import sys
from pathlib import Path

import pytest


HERE = Path(__file__).parent
MAIN_FILE = HERE / "main.py"
TEST_DIR = HERE / "test"
INPUT_FILES = sorted(TEST_DIR.glob("*.in"))


def normalize_output(text: str) -> list[str]:
    """AtCoder の通常ジャッジに合わせ、空白類を区切りとして比較する。"""
    return text.split()


@pytest.mark.parametrize(
    "input_file",
    INPUT_FILES,
    ids=[path.stem for path in INPUT_FILES],
)
def test_case(input_file: Path):
    expected_file = input_file.with_suffix(".out")
    assert expected_file.exists(), f"期待値ファイルがありません: {expected_file.name}"

    result = subprocess.run(
        [sys.executable, MAIN_FILE],
        input=input_file.read_text(),
        text=True,
        capture_output=True,
        timeout=2,
    )

    assert result.returncode == 0, result.stderr
    assert result.stderr == "", (
        "標準エラー出力があります。DEBUG = False にしてから提出してください。\n"
        f"{result.stderr}"
    )
    assert normalize_output(result.stdout) == normalize_output(expected_file.read_text())
