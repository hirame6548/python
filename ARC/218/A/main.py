import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    N = input_data[0]
    M = input_data[1]

    a_l = input_data[2:]
    A_iter = iter(a_l)

    As = []
    for i in range(N):
        cur_line = []
        for _ in range(M):
            cur_line.append(next(A_iter))
        As.append(cur_line)
    #print(As)


    a_cnt = []
    line_dict = defaultdict(list)
    for i in range(N):
        line = As[i]
        line_set = set(line)
        a_dict = defaultdict(int)
        for a in line_set:
            a_dict[a] = line.count(a)
            if a_dict[a]:
                line_dict[a].append(i)
        a_cnt.append(a_dict)
    #print(a_cnt)
    #print(line_dict)


    a_set = set(a_l)
    root_sum = 0
    total = pow(M, N, 998244353)

    for a in a_set:
        #print("a", a)
        prod = 1
        for i in line_dict[a]:
            prod = (prod * (M - a_cnt[i][a])) % 998244353
            #print(a, i, prod)
        len_pow = pow(M, N-len(line_dict[a]), 998244353)
        prod = (prod * len_pow) % 998244353
        root_sum = (root_sum + total - prod) % 998244353

    print(root_sum)

if __name__ == '__main__':
    main()