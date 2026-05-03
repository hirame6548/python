import pytest
import io
from D.main_tle import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """4 6 6
2 2
1 4
3 1
1 2
3 1
4 2
""",
        
        # 期待される出力
        """2 2
4 1
1 1
1 2
1 4
1 5
"""
    ),



    (
        # 入力
        """100 100 20
72 7
4 74
17 67
20 67
96 3
1 95
5 81
87 3
3 87
16 67
95 8
100 2
92 1
3 98
92 5
87 3
1 98
19 67
11 74
87 1
""",

        # 期待される出力
        """7 89
90 22
62 22
7 22
4 96
99 1
94 15
7 19
4 9
27 22
4 1
1 99
7 14
1 1
7 9
7 16
100 1
43 22
79 22
7 15
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