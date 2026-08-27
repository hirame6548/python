from collections import deque
from collections import defaultdict
import copy


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

    src = deque() # (cur, move(list))
    cur = S_xy
    d_dict = defaultdict(list)
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    src.append([cur, []])
    n_move = []
    src_set = set()
    src_set.add(cur)
    sp_set = set(["o", "x"])

    for d_xy in dxy:
        n_xy = (cur[0] + d_xy[0], cur[1] + d_xy[1])
        if d_xy in d_dict[cur]:
            continue
        if Ss[n_xy[0]][n_xy[1]] != "#":
            n_move = []
            n_move.append(d_xy)
            src.append((n_xy, n_move))
            d_dict[cur].append(d_xy)
            src_set.add(n_xy)
            #print(cur, n_xy, src, d_dict)
            #print("______________")

    frag = False
    while src:
        # move の処理はこの一行だけ、他は次の探索地点の話
        cur, move = src.pop()
        n_move = copy.copy(dxy)
        #print("______________")
        #print("move=",move, "cur=",cur)
        if Ss[cur[0]][cur[1]] == "o":
            n_move = [move[-1]]
        if Ss[cur[0]][cur[1]] == "x":
            n_move.remove(move[-1])
        if Ss[cur[0]][cur[1]] == "G":
            print("Yes")
            ans = ""
            for j in range(len(move)):              
                ans += "R" if move[j] == (0, 1) else "L" if move[j] == (0, -1) else "D" if move[j] == (1, 0) else "U"
            print(ans)
            frag = True
            break
        #print("n_move=",n_move)
        for d_xy in n_move:
            n_xy = (cur[0] + d_xy[0], cur[1] + d_xy[1])
            #print("move=",move, "d_xy=",d_xy, "cur=",cur, "n_xy=",n_xy)
            if d_xy in d_dict[cur]:
                continue
            n_val = Ss[n_xy[0]][n_xy[1]]
            if n_val != "#":
                if not n_xy in src_set or n_val in sp_set:
                    new_move = copy.copy(move)
                    new_move.append(d_xy)
                    #print("new_move=",new_move, "move=",move)
                    src.append((n_xy, new_move))
                    d_dict[cur].append(d_xy)
                    #print("New root!")
                    #print("d_xy=",d_xy, "new_move=",new_move)
                src_set.add(n_xy)
                #print(cur, n_xy, src, d_dict)
                #print("______________")


    if not frag:
        print("No")



if __name__ == "__main__":
    main()