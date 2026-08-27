from collections import deque
from collections import defaultdict

def cvt_dir(dxy):
    if dxy == (0, 1):
        return "R"
    if dxy == (0, -1):
        return "L"
    if dxy == (1, 0):
        return "U"
    if dxy == (-1, 0):
        return "D"
    
def s_judge(s_xy, Ss):
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d_xy in dxy:
        c_x, c_y = s_xy[0] + d_xy[0], s_xy[1] + d_xy[1]
        if Ss[c_x][c_y] != "#":
            return True
        else:
            return False



def main():
    H, W = map(int, input().split())

    Ss = []
    for i in range(H):
        Ss.append(input())

    Ss.insert(0, "#" * W)
    Ss.append("#" * W)

    for i in range(H+2):
        Ss[i] = "#" + Ss[i] + "#"
        if "S" in set(Ss[i]):
            S_xy = (i, Ss[i].index("S"))


    src = deque()
    cur = S_xy
    dir = ""
    d_dict = defaultdict(str)

    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if s_judge(S_xy, Ss) == False:
        ans = "No"
    else:
        # 
        # 重要！ src が最初は空だから最初のsrc追加は別に用意
        # 
        while src:


    for d_xy in dxy:
        #print(cur, d_xy)
        c_x, c_y = cur[0] + d_xy[0], cur[1] + d_xy[1]
        #print(x, y)
        if Ss[c_x][c_y] != "#":
            src.append((c_x, c_y))
        if Ss[c_x][c_y] == ".":
            if not cvt_dir(d_xy) in d_dict[cur]:
                cur = (c_x, c_y)
                d_dict[cur] += cvt_dir(d_xy)
            else:
                cur = src
        print(d_xy, c_x, c_y, src, d_dict)



if __name__ == "__main__":
    main()