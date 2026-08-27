import pytest
import io
from E.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """10
ACBBCABCAB
""",
        
        # 期待される出力
        """8
"""
    ),



    (
        # 入力
        """4
CCBC
""",

        # 期待される出力
        """0
"""
    ),



    (
        # 入力
        """36
CABACBBBBBAABABACCBCABCCABAABABBCBAC
""",

        # 期待される出力
        """136
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