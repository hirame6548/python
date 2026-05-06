import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """4 4
2 7 1 8
1 2
2 1 2
1 1
2 2 4
""",
        
        # 期待される出力
        """3
17
"""
    ),



    (
        # 入力
        """8 10
22 75 26 45 72 81 47 29
2 2 7
2 6 8
2 4 4
1 2
2 1 3
1 1
2 2 4
1 2
1 4
2 1 1
""",

        # 期待される出力
        """346
157
45
123
142
26
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