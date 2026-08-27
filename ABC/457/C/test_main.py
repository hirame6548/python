import pytest
import io
from C.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """3 9
3 1 3 2
1 3
2 4 3
1 3 2
""",
        
        # 期待される出力
        """4
"""
    ),



    (
        # 入力
        """3 1
1 7
1 111
1 5
1 100 10000
""",

        # 期待される出力
        """7
"""
    ),



    (
        # 入力
        """3 3163812
5 1 2 3 4 5
4 9 8 7 6
2 10 11
87043 908415 9814
""",

        # 期待される出力
        """9
"""
    ),



    (
        # 入力
        """3 12
        4 1 2 3 4
        2 3 5
        1 5
        3 3 3
        """,

        # 期待される出力
        """4
        """
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