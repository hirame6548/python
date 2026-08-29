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
    K = next(it)

    rl = []

    for i in range(N):
        l = next(it)
        r = next(it)
        rl.append((r, l))
    rl.sort()
    #print(rl)


    

    # ある条件について、数値がそれを満たすかどうかがある点で単調に切り替わるとき、その境界を見つける
    def is_ok(mid):
        #print(rl)
        r_last = rl[0][0]
        k = K-1
        for i in range(N):
            #print("mid, r_last, k, i", mid, r_last, k, i)
            if rl[i][1] >= r_last + mid:
                r_last = rl[i][0]
                k -= 1
        if k > 0:
            return False
        return True
    
    # 条件を満たす値、満たさない値を与えれば、2分探索によりギリギリ満たす値を返す
    def binary_search():
        # okとngを「問題設定上絶対に True になる値」と「絶対に False になる値」で初期化
        ok = 0
        ng = (10**9) +1
        
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    v = binary_search()
    if v:
        print(v)
    else:
        print(-1)




if __name__ == '__main__':
    main()