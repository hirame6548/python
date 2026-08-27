import sys
from pathlib import Path


CONTEST_ROOT = Path(__file__).resolve().parent

for parent in CONTEST_ROOT.parents:
    if (parent / "atcoder_tools" / "download.py").is_file():
        sys.path.insert(0, str(parent))
        break
else:
    raise SystemExit("atcoder_toolsが見つかりません。リポジトリ内で実行してください。")

from atcoder_tools.download import main


if __name__ == "__main__":
    raise SystemExit(main(CONTEST_ROOT))
