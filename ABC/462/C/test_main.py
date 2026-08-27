import pytest
import io
from C.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """3
2 1
1 3
3 2
""",
        
        # 期待される出力
        """2
"""
    ),



    (
        # 入力
        """5
1 1
4 2
2 3
5 5
3 4
""",

        # 期待される出力
        """1
"""
    ),



    (
        # 入力
        """7
3 4
6 1
5 5
2 7
7 2
1 3
4 6
""",

        # 期待される出力
        """2
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