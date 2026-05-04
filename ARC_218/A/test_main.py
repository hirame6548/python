import pytest
import io
from A.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """2 2
1 3
2 3
""",
        
        # 期待される出力
        """7
"""
    ),



    (
        # 入力
        """2 2
1 1
1 2
""",

        # 期待される出力
        """6
"""
    ),



    (
        # 入力
        """3 5
3 1 3 4 2
5 2 1 2 3
4 6 2 5 6
""",

        # 期待される出力
        """327
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