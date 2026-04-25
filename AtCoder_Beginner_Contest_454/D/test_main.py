import pytest
import io
from D.main import main

@pytest.mark.parametrize("input_data, expected_output", [
    (
        # 入力
        """6
(xx)x
x(xx)
(x)x
(xx)
)x()x(
)x()x(
x
(x)
(((((xx)))))x
x((((((((((xx))))))))))
((xx)xx)xx
(x((xx))x)(xx)
""",
        
        # 期待される出力
        """Yes
No
Yes
No
Yes
Yes
"""
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
