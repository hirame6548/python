import sys
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, accumulate
from bisect import bisect_left, bisect_right
import heapq
import math

sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = map(int, input_data)

    N = next(it)
    D = next(it)
    time = [0 for _ in range(10**6 + 1)]

    for i in range(N):
        s = next(it)
        t = next(it) - D + 1
        if s < t:
            time[s] += 1
            time[t] -= 1

    ans = 0
    comb = [0, 0]
    comb_c = 1
    v = 0
    for i in range(10**6 + 1):
        v += time[i]
        while comb_c < v:
            comb_c += 1            
            comb.append(math.comb(comb_c, 2))
        ans += comb[v]

    print(ans)


        


if __name__ == '__main__':
    main()