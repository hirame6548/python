import sys
import itertools

sys.setrecursionlimit(10**6)


def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# 3番目（インデックス2）以降のすべてをリスト a として受け取る例
# a = [int(x) for x in input_data[2:]]
# even = a[0::2]  index が偶数のものだけ取り出す例
    T = int(input_data[0])
    cs = input_data[1:]
    
    idx_0, idx_1 = 0, 1
    for _ in range(T):
        #print(idx_0, idx_1)
        c_0 = cs[idx_0]
        c_1 = cs[idx_1]
        #print(c_0, c_1)

        if cnvt(c_0) == cnvt(c_1):
            print("Yes")
        else:
            print("No")

        idx_0 += 2
        idx_1 += 2



def cnvt(in_str):
    # リストの最初から数えて同じ値のものを区切って出力してくれる
    # ex. [0,0,0,1,1,0,1] → [(0, 3), (1, 2), (0, 1), (1, 1)]
    
    gr = [[x, len(list(y))] for x, y in itertools.groupby(in_str)]
    
    for i in range(1, len(gr)-1):
        x, l = gr[i]
        f_x, f_l = gr[i-1]
        l_x, l_l = gr[i+1]
        if x == "x" and l == 2 and f_x == "(" and l_x == ")":
            sub = min(f_l, l_l)
            gr[i-1][1] -= sub
            gr[i+1][1] -= sub

    ans_list = []
    for x, l in gr:
        ans_list.append(x * l)
    ans = "".join(ans_list)
    
    return ans




if __name__ == '__main__':
    main()