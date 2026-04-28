import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = int(input_data[0])
    Q = int(input_data[1])
    
    CPs = iter(input_data[2:])

    Cs = []
    Ps = []

    for _ in range(Q):
        Cs.append(next(CPs)-1)
        Ps.append(next(CPs)-1)

    ground = [i for i in range(N)]
    par = [-1 for _ in range(N)]
    chi = [-1 for _ in range(N)]
    #print(weight, loc)
    loc_w = [1 for _ in range(N)]


    


    for i in range(Q):
        move_from = Cs[i]
        move_to = Ps[i]
        ground[move_from] = -1
        par[move_to] = move_from
        if chi[move_from] != -1:
            par[chi[move_from]] = -1
        chi[move_from] = move_to
        



    ans_list = []
    for i in range(N):
        if ground[i] != -1:
            #print(ground[i])
            ans_list.append(par_cnt(par, ground[i]))
        else:
            ans_list.append(0)
    print(" ".join(list(map(str, ans_list))))



def par_cnt(par, num):
    counter = 1
    def par_count(par, num):
        nonlocal counter
        if par[num] != -1:
            counter += 1
            par_count(par, par[num])

    par_count(par, num)
    return counter




if __name__ == '__main__':
    main()