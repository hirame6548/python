"""

辞書にない key を選んでも、0 を返してくれる

from collections import defaultdict

# デフォルト値 0 を返す辞書を使用
window_counts = defaultdict(int)


"""




"""

ON / OFF の二択を N 回繰り返す今回のようなケースの場合、bit による管理をすべき
ビット演算子 <<, >> は２進数で桁を一つずらす操作。

# 意識すべき実装
if (i >> j) & 1:  # 整数 i の j ビット目が 1 かどうか

"""