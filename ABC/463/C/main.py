import sys
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, accumulate
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = map(int, input_data)

    N = next(it)
    H = []
    L = []
    for _ in range(N):
        h = next(it)
        l = next(it)
        H.append(h)
        L.append(l)
    #print(H, L)        


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


    s = SegTree(N, max, 0, H)

    Q = next(it)
    #print(Q)

    for _ in range(Q):
        t = next(it)
        idx = bisect_right(L, t)
        print(s.query(idx, N))



if __name__ == '__main__':
    main()