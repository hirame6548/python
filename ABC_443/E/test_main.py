import pytest
import io
from E.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """5
5 3
.###.
..#..
#.#.#
#...#
##..#
2 2
##
..
4 1
####
####
####
.###
3 3
...
...
...
10 3
##.##.##.#
.####..#..
...#.#..#.
.#.#.#.#..
...####...
#.#.##....
.##...#...
#.##.....#
#....###.#
.#..#.#...
""",
        
        # 期待される出力
        """10111
11
1000
111
0011010010
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