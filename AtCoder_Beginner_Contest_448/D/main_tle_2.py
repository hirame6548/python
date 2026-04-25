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
    length = [-1 for _ in range(N)]
    length[0] = 0
    c_list = [As[0]]
    queue = deque([0])
    ans = [0 for _ in range(N)]
    #print(length, ans)

    while queue:
        v = queue.pop()
        c_list.append(As[v])
        c_list[length[v]] = As[v]
        l = len(c_list) - length[v] - 1
        for _ in range(l):
            c_list.pop()
        for nxt_v in nxt[v]:
            #print(v, nxt_v, c_list)
            if length[nxt_v] == -1:
                #print("new!", a_set)
                length[nxt_v] = length[v] + 1
                queue.append(nxt_v)
                if ans[v] == 1:
                    ans[nxt_v] = 1
                    #print("OK")
                elif As[nxt_v] in c_list:
                    ans[nxt_v] = 1
                    #print("OK")
    #print(ans)

    for i in range(len(ans)):
        if ans[i] == 0:
            print("No")
        else:
            print("Yes")
    

if __name__ == '__main__':
    main()