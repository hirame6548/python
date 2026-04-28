import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5 4
1 3
4 5
1 4
4 2
""",
        
        # 期待される出力
        """0 3 1 0 1
"""
    ),



    (
        # 入力
        """7 8
3 1
5 4
2 5
5 7
2 3
6 2
3 4
5 1
""",

        # 期待される出力
        """2 0 0 4 0 0 1
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