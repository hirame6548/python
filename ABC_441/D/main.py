import sys
sys.setrecursionlimit(10**6)
#import itertools  # case = list(itertools.islice(case_iter, N))
from collections import deque
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])
    L = int(input_data[2])
    S = int(input_data[3])
    T = int(input_data[4])

    uvc_iter = iter(map(int, input_data[5:]))

    edge = defaultdict(list)

    for _ in range(M):
        u = next(uvc_iter)
        v = next(uvc_iter)
        c = next(uvc_iter)
        edge[u].append((v, c))
    #print(edge)

    ans = []
    que = deque([(1, 0, 0)]) # (位置, 経路長, コスト) = (x, l, c)
    while que:
        #print(que)
        x, l, c = que.pop()

        # 経路長が L のとき、コストの判定をし ans に追加
        if l == L:
            if S <= c and c <= T:
                ans.append(x)
                #print("find x!")
        
        # 次の頂点に移動
        else:
            ver = edge[x]
            for n_x, n_c in ver:
                if c + n_c <= T:
                    que.append((n_x, l+1, c+n_c))

    ans = set(ans)
    ans = list(ans)
    ans.sort()
    print(*ans)



if __name__ == '__main__':
    main()
