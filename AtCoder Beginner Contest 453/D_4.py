from collections import deque


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

    dir_list = [[[None] * 4 for i in range(W+2)] for _ in range(H+2)]
    #print(dir_list)

    src = deque() # (cur, move(list))
    cur = S_xy
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    for d_xy in dxy:
        n_x, n_y = cur[0] + d_xy[0], cur[1] + d_xy[1]
        #print(n_xy, src)
        n_val = Ss[n_x][n_y]
        if n_val != "#" and not dir_list[n_x][n_y][dxy.index(d_xy)]:
            src.append(((n_x, n_y), d_xy))
            dir_list[n_x][n_y][dxy.index(d_xy)] = "S"

    frag = False
    while src:
        #print("探索待ち=",src)
        cur, move = src.popleft()
        n_move = [d for d in dxy]
        if Ss[cur[0]][cur[1]] == "o":
            n_move = [move]
            #print("move, n_move",move, n_move)
        if Ss[cur[0]][cur[1]] == "x":
            n_move.remove(move)
        if Ss[cur[0]][cur[1]] == "G":
            print("Yes")
            ans_list = []
            #print("dir_list")
            #for i in range(len(dir_list)):
            #    print(dir_list[i])
            #print("cur, move",cur, move)
            ans_list.append("R" if move == (0, 1) else  "L" if move == (0, -1) else "D" if move == (1, 0) else "U")
            cur, move = (cur[0] - move[0], cur[1] - move[1]), dir_list[cur[0]][cur[1]][dxy.index(move)]
            #print(ans_list)
            while Ss[cur[0]][cur[1]] != "S":
            #for i in range(10):
                #print("f_move",f_move)
                #print("cur, move",cur, move)
                ans_list.append("R" if move == (0, 1) else  "L" if move == (0, -1) else "D" if move == (1, 0) else "U")
                cur, move = (cur[0] - move[0], cur[1] - move[1]), dir_list[cur[0]][cur[1]][dxy.index(move)]
                #print("cur",cur, "move",move)
                #print(ans_list)
            ans_list.reverse()
            print("".join(ans_list))
            frag = True
            break
        #print("今の座標",cur, "直前の進行方向",move, "これから動く方向",n_move)
        for d_xy in n_move:
            n_x, n_y = cur[0] + d_xy[0], cur[1] + d_xy[1]
            n_val = Ss[n_x][n_y]
            #print("移動方向",d_xy, "移動後座標",n_xy, "移動後の値",n_val)
            if n_val != "#" and not dir_list[n_x][n_y][dxy.index(d_xy)]:
                src.append(((n_x, n_y), d_xy))
                dir_list[n_x][n_y][dxy.index(d_xy)] = move


    if not frag:
        print("No")


if __name__ == "__main__":
    main()