H, W = list(map(int, input().split()))


matrix = []
for _ in range(H):
    matrix.append(input())

for i in range(H):
    matrix[i] = matrix[i].replace("#", "0")
    matrix[i] = matrix[i].replace(".", "1")
    matrix[i] = "0" + matrix[i] + "0"
matrix.insert(0, "0" * (W+2))
matrix.append("0" * (W+2))

for i in range(H+2):
    matrix[i] = list(map(int, list(matrix[i])))


import heapq
cur_vis = (0, 0)
next_vis = []

dhw = [(0, 1), (0, -1), (1, 0), (-1, 0)]



ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        #print(h, w)
        cur_vis = (h, w)
        #print("____________")
        #print("cur=", cur_vis)
        frag = 0
        if matrix[h][w] == 1:
            frag = 1
            if h == 1 or h == H or w == 1 or w == W:
                frag = 0
            for dh, dw in dhw:
                if matrix[h+dh][w+dw] == 1:
                    heapq.heappush(next_vis, (cur_vis[0]+dh, cur_vis[1]+dw))
                    matrix[cur_vis[0]+dh][cur_vis[1]+dw] = 0
            matrix[cur_vis[0]][cur_vis[1]] = 0
            #for i in range(H+2):
            #    print(matrix[i])
            while next_vis:
                cur_h, cur_w = heapq.heappop(next_vis)
                cur_vis = (cur_h, cur_w)
                if cur_h == 1 or cur_h == H or cur_w == 1 or cur_w == W:
                    frag = 0
                for dh, dw in dhw:
                    if matrix[cur_h+dh][cur_w+dw] == 1:
                        heapq.heappush(next_vis, (cur_h+dh, cur_w+dw))
                        matrix[cur_h+dh][cur_w+dw] = 0
                matrix[cur_h][cur_w] = 0
                #print("cur=", cur_vis)
                #for i in range(H+2):
                #    print(matrix[i])
        ans += frag


print(ans)


"""

BFSなら deque を使う!（計算量が少ない）heapqは並び替えをするからやや遅い

from collections import deque



"""