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


    def rec():
        rest = c_l[0]
        n = len(c_l)
        n_max = rest // n
        if n == N:
            c_l[0] -= n * n_max
            c_l.append(n_max)
            if c_l[0] == 0:
                print(*c_l[1:])
            return
        for i in range(n_max, -1, -1):
            n_l = c_l.copy()
            n_l[0] -= n*i
            n_l.append(i)
            l.appendleft(n_l)
            #print("in rec l", l)

    l = deque()
    l.append([K])
    ans = []
    while l:
        c_l = l.popleft()
        #print("c_l", c_l)
        #print("l", l)
        rec()
        #print("ans", ans)


if __name__ == "__main__":
    main()