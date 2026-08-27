import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    K = int(input_data[1])

    As = list(map(int, input_data[2:]))
    #print(As)


    # ある条件について、数値がそれを満たすかどうかがある点で単調に切り替わるとき、その境界を見つける
    def is_ok(N, As, K, mid):
        k_sum = 0
        for i in range(N):
            if mid > As[i]:
                k_sum += (mid - As[i] + i) // (i+1)
                #print("mid",mid, "i+1",i+1, "k_sum",k_sum)
        if k_sum <= K:
            return True
        else:
            return False
    
    # 条件を満たす値、満たさない値を与えれば、2分探索によりギリギリ満たす値を返す
    def binary_search(N, As, K):
        # okとngを「問題設定上絶対に True になる値」と「絶対に False になる値」で初期化
        ok = 0
        ng = 2 * (10**18) + 1
        
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(N, As, K, mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    print(binary_search(N, As, K))



if __name__ == '__main__':
    main()