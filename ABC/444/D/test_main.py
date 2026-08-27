import pytest
import io
from D.main_wa import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """4
3 3 3 3
""",
        
        # 期待される出力
        """444
"""
    ),



    (
        # 入力
        """3
30 10 20
""",

        # 期待される出力
        """111111111122222222223333333333
"""
    ),



    (
        # 入力
        """10
1 2 3 4 5 6 7 8 9 10
""",

        # 期待される出力
        """1234567900
"""
    ),



    (
        # 入力
        """10
3 3 3 3 3 3 3 3 3 1
""",

        # 期待される出力
        """1000
"""
    ),



    (
        # 入力
        """4
1 2 5 10
""",

        # 期待される出力
        """1111122234
"""
    ),


])

def test_main(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    main()
    captured = capsys.readouterr()

    # 両方の末尾の改行や空白を削ぎ落としてから比較する
    assert captured.out.strip() == expected_output.strip()