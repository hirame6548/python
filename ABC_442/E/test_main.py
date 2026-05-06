import pytest
import io
from E.main_wa import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5 4
0 1
1 -2
1 0
-2 0
3 0
4 1
1 4
5 4
3 5
""",
        
        # 期待される出力
        """2
5
4
2
"""
    ),



    (
        # 入力
        """2 1
1 2
1 2
1 2
""",

        # 期待される出力
        """2
"""
    ),



    (
        # 入力
        """8 10
-84 -60
-100 8
77 55
-14 -10
50 -4
-63 -45
26 -17
-7 -5
3 7
2 4
8 4
8 4
7 1
1 7
6 3
4 7
4 5
2 6
""",

        # 期待される出力
        """3
8
4
4
5
8
6
8
7
8
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