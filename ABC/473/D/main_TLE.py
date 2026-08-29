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

    # ---------- input ----------
    N = int(next(it))
    K = int(next(it))
    # ---------- solve ----------


    def rec(N, in_l):
        rest = in_l[0]
        length = len(in_l)
        n = N+1 - length
        n_max = rest // n
        l = [[in_l[0] - n*i] + in_l[1:] + [i] if length != 0 else "" for i in range(n_max+1)]
        return l

    l = [[K]]
    ans = []
    while l:
        c_l = l.pop()
        #print("c_l", c_l)
        #print("l", l)
        if len(c_l) == N:
            c_l.append(c_l[0])
            ans.append(list(reversed(c_l[1:])))
        else:
            l += rec(N, c_l)
        #print("ans", ans)

    ans.sort()
    for l in ans:
        print(*l)


if __name__ == "__main__":
    main()