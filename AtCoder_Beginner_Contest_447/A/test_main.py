import pytest
import io
from A.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """6 3
""",
        
        # 期待される出力
        """Yes
"""
    ),



    (
        # 入力
        """4 3
""",

        # 期待される出力
        """No
"""
    ),



    (
        # 入力
        """5 3
""",

        # 期待される出力
        """Yes
"""
    ),



    (
        # 入力
        """44 7
""",

        # 期待される出力
        """Yes
"""
    ),



    (
        # 入力
        """87 44""",

        # 期待される出力
        """Yes"""
    ),


])

def test_main(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    main()
    captured = capsys.readouterr()

    # 両方の末尾の改行や空白を削ぎ落としてから比較する
    assert captured.out.strip() == expected_output.strip()