import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5
1 3 2 1 2
1 2
1 3
3 4
3 5
""",
        
        # 期待される出力
        """No
No
No
Yes
Yes
"""
    ),



    (
        # 入力
        """2
1000000000 1000000000
2 1
""",

        # 期待される出力
        """No
Yes
"""
    ),



    (
        # 入力
        """10
10 7 3 9 1 3 8 5 7 10
3 6
8 6
6 1
9 7
7 10
5 4
4 2
10 2
1 9
""",

        # 期待される出力
        """No
Yes
Yes
Yes
Yes
No
No
No
No
Yes
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