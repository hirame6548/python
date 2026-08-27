import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    N = input_data[0]
    Q = input_data[1]

    c_iter = iter(input_data[2:])

    As = list(itertools.islice(c_iter, N))
    As.sort()
    #print(As)


    # ある条件について、数値がそれを満たすかどうかがある点で単調に切り替わるとき、その境界を見つける
    def is_ok(x, mid, equal=False):
        if equal:
            if As[mid] <= x:
                return True
        else:
            if As[mid] < x:
                return True
    
    # 条件を満たす値、満たさない値を与えれば、2分探索によりギリギリ満たす値を返す
    def binary_search(x, equal=False):
        # okとngを「問題設定上絶対に True になる値」と「絶対に False になる値」で初期化
        ok = -1
        ng = N
        
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            #print(mid)
            if is_ok(x, mid, equal):
                ok = mid
            else:
                ng = mid
        return ok



    for _ in range(Q):
        X = next(c_iter)
        Y = next(c_iter)
        while X in As:
            X += 1
        #print(X, Y)
        #print(As[binary_search(X)])

        ans = X + Y - 1
        x_gap = binary_search(X)
        gap = binary_search(ans, equal=True) - x_gap

        while ans - gap != X + Y - 1:
        #for i in range(5):
            ans += (X+Y-1) - (ans - gap)
            gap = binary_search(ans, equal=True) - x_gap
            #print(ans, gap, x_gap)
        
        print(ans)



if __name__ == '__main__':
    main()