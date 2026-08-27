import pytest
import io
from C.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5 5
1 2
2 3
3 4
2 4
5 2
""",
        
        # 期待される出力
        """4
"""
    ),



    (
        # 入力
        """3 2
2 1
3 2
""",

        # 期待される出力
        """1
"""
    ),



    (
        # 入力
        """7 8
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
""",

        # 期待される出力
        """6
"""
    ),


])

def test_main(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    main()
    captured = capsys.readouterr()

    # 両方の末尾の改行や空白を削ぎ落としてから比較する
    assert captured.out.strip() == expected_output.strip()
