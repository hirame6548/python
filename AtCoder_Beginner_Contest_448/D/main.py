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
    
    ans = [0 for _ in range(N)]
    #print(length, ans)

    c_set = set()
    counter = 0
    visited = [False for _ in range(N)]


    def dfs(v):
        nonlocal counter
        frag = False
        visited[v] = True
        #print(v, counter)

        if As[v] in c_set:
            counter += 1
            frag = True
        else:
            c_set.add(As[v])

        if counter > 0:
            ans[v] = 1

        for u in nxt[v]:
            if not visited[u]:
                dfs(u)

        if frag:
            counter -= 1
        else:
            c_set.remove(As[v])

    dfs(0)

    for i in range(len(ans)):
        if ans[i] == 0:
            print("No")
        else:
            print("Yes")
    

if __name__ == '__main__':
    main()