import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5 8 3 80 100
1 2 20
1 3 70
2 1 30
2 5 10
3 2 10
3 4 30
3 5 20
5 1 70
""",
        
        # 期待される出力
        """1 5
"""
    ),



    (
        # 入力
        """10 1 1 1 100
2 3 1
""",

        # 期待される出力
        """
"""
    ),



    (
        # 入力
        """2 5 3 1 100
1 1 1
2 2 100
1 2 1
1 2 1
1 2 100
""",

        # 期待される出力
        """1 2
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