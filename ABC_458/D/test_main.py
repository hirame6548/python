import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5
3
2 3
1 2
8 9
""",
        
        # 期待される出力
        """3
2
3
"""
    ),



    (
        # 入力
        """1
4
2 3
4 5
6 7
8 9
""",

        # 期待される出力
        """2
3
4
5
"""
    ),



    (
        # 入力
        """278117031
7
167642909 517897721
148434323 567739597
319926999 481642530
659199879 252516557
49913403 798318034
89701408 892537201
199166668 742285869
""",

        # 期待される出力
        """278117031
278117031
319926999
319926999
319926999
319926999
319926999
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