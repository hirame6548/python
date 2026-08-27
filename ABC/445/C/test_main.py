import pytest
import io
from C.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """7
2 4 7 5 5 6 7
""",
        
        # 期待される出力
        """5 5 7 5 5 6 7
"""
    ),



    (
        # 入力
        """5
1 2 3 4 5
""",

        # 期待される出力
        """1 2 3 4 5
"""
    ),



    (
        # 入力
        """15
11 3 10 7 15 10 10 11 11 13 11 12 14 14 15
""",

        # 期待される出力
        """11 14 14 14 15 14 14 11 11 14 11 12 14 14 15
"""
    ),



    (
        # 入力
        """""",

        # 期待される出力
        """"""
    ),



    (
        # 入力
        """""",

        # 期待される出力
        """"""
    ),


])

def test_main(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    main()
    captured = capsys.readouterr()

    # 両方の末尾の改行や空白を削ぎ落としてから比較する
    assert captured.out.strip() == expected_output.strip()