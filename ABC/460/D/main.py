import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    H = int(input_data[0])
    W = int(input_data[1])
    s_iter = iter(input_data[2:])
    S = []

    visited = [[-2 for _ in range(W+2)]]+[[-2]+[-1 for _ in range(W)]+[-2] for i in range(H)]+[[-2 for _ in range(W+2)]]
    #print(visited)

    src_d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    que = deque()
    frag = True

    for h in range(H):
        sn = next(s_iter)
        s_line = []
        for w in range(W):
            if sn[w] == ".":
                s_line.append(0)
                if frag:
                    frag = False
            else:
                s_line.append(1)
                visited[h+1][w+1] = 0
                que.append((h+1, w+1, 0))
        S.append(s_line)


    while que:
        high, wid, step = que.popleft()
        for dir in src_d:
            dh, dw = dir
            c_h = high + dh
            c_w = wid + dw
            c_s = (step + 1) % 2
            if visited[c_h][c_w] == -2:
                continue
            elif visited[c_h][c_w] == -1:
                visited[c_h][c_w] = c_s
                que.append((c_h, c_w, c_s))
            #print(c_h, c_w, c_s, que)
            #for line in visited:
                #print(line)
    
    for line in visited:
        ans = []
        for s in line:
            if s == 0:
                ans.append("#")
            elif s == 1:
                ans.append(".")
        if ans:
            print("".join(ans))






if __name__ == '__main__':
    main()