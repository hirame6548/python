import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    T = input_data[0]
    c_iter = iter(input_data[1:])

    for _ in range(T):
        N = next(c_iter)
        W = next(c_iter)
        if N < W:
            W = N




        bit_size = (4 * W) + 1
        bit = [0] * bit_size
        
        # 内部では 1-indexed で扱うが、入力は 0-indexed で受付
        # 配列の更新、区間和の算出を高速で行う
        # 要素の値が欲しいときは別の配列を用意する (query_sum(i+1) - query(i)でもいいが、log(N)かかる)
        
        # i 番目の要素に x を加算、初期化もこれで行う
        def add(i, x):
            i += 1
            while i < bit_size:
                bit[i] += x
                i += i & -i
        
        # 区間 [0, i) の和を出力する。i は左端からの個数に等しい
        def query_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
    



        Cs = list(itertools.islice(c_iter, N))
        #print(N, W, Cs)

        for i in range(N):
            idx = i % (2*W)
            add(idx, Cs[i])
            add(idx + 2*W, Cs[i])



        min_sum = float("inf")
        for i in range(2*W):
            c_sum = query_sum(i+W) - query_sum(i)
            #print(c_sum)
            if c_sum < min_sum:
                min_sum = c_sum
        
        print(min_sum)


if __name__ == '__main__':
    main()