import pytest
import io
from E.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5 7
2 3
1 2
1 5
4 5
2 4
3 5
1 3
""",
        
        # 期待される出力
        """22
"""
    ),



    (
        # 入力
        """2 1
1 2
""",

        # 期待される出力
        """2
"""
    ),



    (
        # 入力
        """8 16
2 7
5 7
6 8
1 7
4 7
1 3
2 8
5 8
4 8
2 5
3 4
3 8
1 4
1 8
4 6
1 2
""",

        # 期待される出力
        """54
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