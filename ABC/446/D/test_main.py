import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """7
3 4 3 5 7 6 2
""",
        
        # 期待される出力
        """4
"""
    ),



    (
        # 入力
        """5
5 4 3 2 1
""",

        # 期待される出力
        """1
"""
    ),



    (
        # 入力
        """10
1 2 3 4 5 6 7 8 9 10
""",

        # 期待される出力
        """10
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