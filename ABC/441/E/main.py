import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict



class SegTree:
    __slots__ = ['n', 'size', 'tree', 'op', 'e']

    def __init__(self, n, op, e, v=None):
        """
        n: 配列のサイズ
        op: 2つの区間をマージする関数 (例: lambda x, y: x + y,   min, max 等)
        e: 単位元 (初期値。op(x, e) == x となる値。和なら0、最小値ならINF)
        v: 初期配列 (省略可)
        """
        self.n = n
        self.op = op
        self.e = e
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [self.e] * (2 * self.size)
        if v is not None:
            for i in range(n):
                self.tree[self.size + i] = v[i]
            for i in range(self.size - 1, 0, -1):
                self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, p):
        """要素 p の現在の値を返す (O(1))"""
        return self.tree[p + self.size]

    def update(self, p, x):
        """要素 p を x に更新する (O(log N))"""
        p += self.size
        self.tree[p] = x
        while p > 1:
            p >>= 1
            self.tree[p] = self.op(self.tree[2 * p], self.tree[2 * p + 1])

    def query(self, l, r):
        """区間 [l, r) の op の結果を返す (O(log N))"""
        res_l = self.e
        res_r = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.tree[r], res_r)
            l >>= 1
            r >>= 1
        return self.op(res_l, res_r)




def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    S = input_data[1]

    s_l = []
    for s in S:
        #print(s)
        if s == "A":
            s_l.append(1)
        elif s == "B":
            s_l.append(-1)
        else:
            s_l.append(0)
        #print(s_l)
    #print(s_l)

    ans = 0
    sum_dict = defaultdict(int)
    min_sum = float("inf")
    max_sum = -1 * float("inf")
    sum = 0
    x_sum = []
    for i in range(N):
        sum += s_l[i]
        if sum < min_sum:
            min_sum = sum
        if sum > max_sum:
            max_sum = sum
        sum_dict[sum] += 1
        x_sum.append(sum)

    d_l = len(sum_dict)
    #print(d_l, min_sum, max_sum)
    sum_l = []
    for i in range(min_sum, max_sum+1):
        #print(i)
        sum_l.append(sum_dict[i])
    sum_l.append(0)
    #print(sum_l) # [5, 3, 2, 0]

    seg = SegTree(d_l, lambda x, y: x+y, 0, sum_l)
    seg_max = max_sum - min_sum + 1

    ans = 0
    for i in range(N):
        idx = x_sum[i] - min_sum
        #print(idx)
        seg.update(idx, seg.get(idx) - 1)
        if s_l[i] == 1:
            ans += seg.query(idx, seg_max) + 1
        elif s_l[i] == -1:
            ans += seg.query(idx+2, seg_max)
        else:
            ans += seg.query(idx+1, seg_max)

    print(ans)

    

if __name__ == '__main__':
    main()
