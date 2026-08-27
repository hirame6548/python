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
    it = map(int, input_data)

    N = next(it)
    M = next(it)

    min_l = 300
    for j in range(N):
        l = next(it)
        if l < min_l:
            min_l = l

    ans = 0
    for i in range(M):
        s = next(it)
        if min_l >= s:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()