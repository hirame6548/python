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
    D = next(it)
    st = [[next(it), next(it)] for _ in range(N)]

    print(N)


if __name__ == '__main__':
    main()