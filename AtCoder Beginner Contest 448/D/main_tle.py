import sys
from collections import deque
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = input_data[0]
    As = input_data[1:N+1]
    
    nxt = [[] for _ in range(N)]

    Us = input_data[N+1::2]
    Vs = input_data[N+2::2]
    #print(As, Us, Vs, nxt)

    for i in range(len(Us)):
        nxt[Us[i]-1].append(Vs[i]-1)
        nxt[Vs[i]-1].append(Us[i]-1)
    #print(nxt)
    
    # N = グラフの頂点数, G = 隣接頂点(辺)の list, start = 探索開始頂点
    # 出力 = start から各頂点への最短距離の list
    dist = [-1] * N
    dist[0] = 0
    a0_set = set([As[0]])
    queue = deque([(0, a0_set)])

    while queue:
        v, a_set = queue.popleft()
        for nxt_v in nxt[v]:
            #print(v, nxt_v)
            if dist[nxt_v] == -1:
                #print("new!", a_set)
                if dist[v] == 1:
                    dist[nxt_v] = 1
                    n_set = set()
                    #print("wow")
                elif As[nxt_v] in a_set:
                    dist[nxt_v] = 1
                    n_set = set()
                    #print("wow")
                else:
                    dist[nxt_v] = 0
                    n_set = {As[nxt_v]}
                    n_set.update(a_set)
                    #print(v, nxt_v, a_set, n_set)
                queue.append((nxt_v, n_set))

    for i in range(len(dist)):
        if dist[i] == 0:
            print("No")
        else:
            print("Yes")
    


if __name__ == '__main__':
    main()