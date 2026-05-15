import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """3 3
1 2 3
""",
        
        # 期待される出力
        """3
"""
    ),



    (
        # 入力
        """4 5
10 1 10 1
""",

        # 期待される出力
        """7
"""
    ),



    (
        # 入力
        """20 457
8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6
""",

        # 期待される出力
        """132
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