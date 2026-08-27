import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """3 2
9 17
10 12
13 20
""",
        
        # 期待される出力
        """4
"""
    ),



    (
        # 入力
        """3 5
9 17
10 12
13 20
""",

        # 期待される出力
        """0
"""
    ),



    (
        # 入力
        """4 1
1 1000000
1 1000000
1 1000000
1 1000000
""",

        # 期待される出力
        """5999994
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