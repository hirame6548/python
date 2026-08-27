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
    l_dict = defaultdict(list)


    for i in range(N):
        if As[i] % 7 == 0:
            #print(i, As[i]//7, l_dict[As[i] // 7])
            for cnt in l_dict[As[i] // 7]:
                cnt[0] += 1
            #print(i, As[i]//7, l_dict[As[i] // 7])
        if As[i] % 3 == 0:
            #print(i, As[i]//3, l_dict[As[i] // 3])
            for cnt in l_dict[As[i] // 3]:
                cnt[1] += 1
            #print(i, As[i]//3, l_dict[As[i] // 3])
        if As[i] % 5 == 0:
            l_dict[As[i] // 5].append([0, 0])
    for v in l_dict.values():
        for i, j in v:
            ans += i * j
    #print(l_dict)

    l_dict.clear()
    for i in range(N-1, -1, -1):
        if As[i] % 7 == 0:
            #print(i, As[i]//7, l_dict[As[i] // 7])
            for cnt in l_dict[As[i] // 7]:
                cnt[0] += 1
            #print(i, As[i]//7, l_dict[As[i] // 7])
        if As[i] % 3 == 0:
            #print(i, As[i]//3, l_dict[As[i] // 3])
            for cnt in l_dict[As[i] // 3]:
                cnt[1] += 1
            #print(i, As[i]//3, l_dict[As[i] // 3])
        if As[i] % 5 == 0:
            l_dict[As[i] // 5].append([0, 0])
    for v in l_dict.values():
        for i, j in v:
            ans += i * j
    print(ans)


if __name__ == '__main__':
    main()