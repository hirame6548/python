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

    l = []
    for i in range(N):
        x = next(it)
        y = next(it)
        l.append([x, y])

    l.sort()

    min = 10**10
    ans = 0
    for x, y in l:
        if min > y:
            min = y
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()