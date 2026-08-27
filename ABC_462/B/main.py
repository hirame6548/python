import sys
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, accumulate
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)

    N = int(next(it))

    ans = [[] for _ in range(N)]

    for i in range(N):
        k = int(next(it))
        for _ in range(k):
            a = int(next(it)) - 1
            ans[a].append(i)

    for i in range(N):
        ans_r = []
        l = len(ans[i])
        ans_r.append(l)
        for j in range(l):
            ans_r.append(ans[i][j] + 1)
        print(*ans_r)



if __name__ == '__main__':
    main()
