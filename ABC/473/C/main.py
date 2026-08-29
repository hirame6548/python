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

    # ---------- input ----------
    N = next(it)
    K = next(it)
    # ---------- solve ----------
    c = {}
    for i in range(N):
        a = next(it)
        if not a in c:
            c[a] = 1
        else:
            c[a] += 1

    l = list(c.values())

    max_l = max(l)

    ans = 0
    for i in l:
        if i+1 >= max_l:
            ans += 1

    print(ans)


debug_on = 0

def debug(out):
    if debug_on:
        print(out)





if __name__ == "__main__":
    main()