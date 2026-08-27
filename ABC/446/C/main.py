import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    T = int(input_data[0])
    cases = iter(list(map(int, input_data[1:])))

    each_c = []
    for _ in range(T):
        N = next(cases)
        D = next(cases)
        As = []
        Bs = []
        for i in range(N):
            As.append(next(cases))
        for i in range(N):
            Bs.append(next(cases))
        each_c.append([N, D, As, Bs])

    #print(each_c) # [[3, 1, [7, 2, 3], [1, 3, 2]], [3, 2, [7, 2, 3], [1, 3, 2]], [2, 1, [2, 1], [1, 2]]]
    

    for t in range(T):
        #print("case", t)
        n, d, a_list, b_list = each_c[t]
        eggs = [0 for _ in range(n)]
        old_day = 0
        for day in range(n):
            eggs[day] = a_list[day]
            use_eggs = b_list[day]
            #print("day", day, "eggs", eggs, "use_eggs", use_eggs)
            while eggs[old_day] < use_eggs:
                use_eggs -= eggs[old_day]
                eggs[old_day] = 0
                old_day += 1
            eggs[old_day] -= use_eggs
            if day - old_day == d:
                eggs[old_day] = 0
                old_day += 1
        print(sum(eggs))




    

if __name__ == '__main__':
    main()