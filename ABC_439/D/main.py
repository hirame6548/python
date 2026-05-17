import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    As = list(map(int, input_data[1:]))
    #print(N, As)

    ans = 0
    l_dict = defaultdict(lambda: [0, 0]) # 現在の累積和
    cnt_5 = defaultdict(list) # 5が来た時点での累積和を保存

    for i in range(N):
        if As[i] % 7 == 0:
            #print(i, As[i]//7, l_dict[As[i] // 7])
            l_dict[As[i] // 7][0] += 1
            #print(i, As[i]//7, l_dict[As[i] // 7])
        if As[i] % 3 == 0:
            #print(i, As[i]//3, l_dict[As[i] // 3])
            l_dict[As[i] // 3][1] += 1
            #print(i, As[i]//3, l_dict[As[i] // 3])
        if As[i] % 5 == 0:
            cnt_5[As[i] // 5].append([i for i in l_dict[As[i] // 5]])
            #print(l_dict[As[i] // 5])
    #print(l_dict, cnt_5)

    for k, v in cnt_5.items():
        sum_7 = l_dict[k][0]
        sum_3 = l_dict[k][1]
        for i, j in v:
            ans += (sum_7-i) * (sum_3-j)
    #print(ans)

    l_dict.clear() # 現在の累積和
    cnt_5.clear() # 5が来た時点での累積和を保存

    for i in range(N-1, -1, -1):
        if As[i] % 7 == 0:
            #print(i, As[i]//7, l_dict[As[i] // 7])
            l_dict[As[i] // 7][0] += 1
            #print(i, As[i]//7, l_dict[As[i] // 7])
        if As[i] % 3 == 0:
            #print(i, As[i]//3, l_dict[As[i] // 3])
            l_dict[As[i] // 3][1] += 1
            #print(i, As[i]//3, l_dict[As[i] // 3])
        if As[i] % 5 == 0:
            cnt_5[As[i] // 5].append([i for i in l_dict[As[i] // 5]])
            #print(l_dict[As[i] // 5])
    #print(l_dict, cnt_5)

    for k, v in cnt_5.items():
        sum_7 = l_dict[k][0]
        sum_3 = l_dict[k][1]
        for i, j in v:
            ans += (sum_7-i) * (sum_3-j)
    print(ans)


if __name__ == '__main__':
    main()