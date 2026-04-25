from collections import deque
from collections import defaultdict


def main():
    H, W = map(int, input().split())

    Ss = []
    for _ in range(H):
        Ss.append(input())

    Ss.insert(0, "#" * W)
    Ss.append("#" * W)

    for i in range(H+2):
        Ss[i] = "#" + Ss[i] + "#"
        if "S" in set(Ss[i]):
            S_xy = (i, Ss[i].index("S"))

    dir_list = [[[] for i in range(W+2)] for _ in range(H+2)] # 探索済みのマスには方向が入っており、そうでなければNone
    parent = [[defaultdict(tuple) for i in range(W+2)] for _ in range(H+2)]
    #print(dir_list)

    src = deque() # (cur, move(list))
    cur = S_xy
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n_move = []


    for d_xy in dxy:
        n_xy = (cur[0] + d_xy[0], cur[1] + d_xy[1])
        #print(n_xy, src)
        n_val = Ss[n_xy[0]][n_xy[1]]
        if n_val != "#" and not d_xy in dir_list[n_xy[0]][n_xy[1]]:
            src.append((n_xy, d_xy))
            dir_list[n_xy[0]][n_xy[1]].append(d_xy)


    frag = False
    while src:
        #print("探索待ち=",src)
        cur, move = src.popleft()
        n_move = [d for d in dxy]
        if Ss[cur[0]][cur[1]] == "o":
            n_move = [move]
        if Ss[cur[0]][cur[1]] == "x":
            n_move.remove(move)
        if Ss[cur[0]][cur[1]] == "G":
            print("Yes")
            ans = "R" if move == (0, 1) else "L" if move == (0, -1) else "D" if move == (1, 0) else "U"
            #while cur != S_xy:
            print(parent)
            for i in range(10):
                print(parent[cur[0]][cur[1]])
                ans = "R" +ans if parent[cur[0]][cur[1]][move] == (0, 1) else "L"+ans if parent[cur[0]][cur[1]] == (0, -1) else "D"+ans if parent[cur[0]][cur[1]] == (1, 0) else "U" + ans
                move = parent[cur[0]][cur[1]][move]
                cur = (cur[0] - parent[cur[0]][cur[1]][move][0], cur[1] - parent[cur[0]][cur[1]][move][1])
                print(cur)
            print(ans)
            frag = True
            break
        #print("今の座標",cur, "直前の進行方向",move, "これから動く方向",n_move)
        for d_xy in n_move:
            n_xy = (cur[0] + d_xy[0], cur[1] + d_xy[1])
            n_val = Ss[n_xy[0]][n_xy[1]]
            #print("移動方向",d_xy, "移動後座標",n_xy, "移動後の値",n_val)
            if n_val != "#" and not d_xy in dir_list[n_xy[0]][n_xy[1]]:
                src.append((n_xy, d_xy))
                dir_list[n_xy[0]][n_xy[1]].append(d_xy)
                if parent[n_xy[0]][n_xy[1]][d_xy] == ():
                    parent[n_xy[0]][n_xy[1]][d_xy] = move


    if not frag:
        print("No")


if __name__ == "__main__":
    main()