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
    K = next(it)
    M = next(it)

    s_l = []
    for i in range(N):
        s = next(it)
        s_l.append((s, N-i-1))
    #print(s_l)

    val_l = [1 for _ in range(N)]
    for j in range(M):
        d = next(it) - 1
        #print(d)
        val_l[d] = 0
    #print(val_l)

    l = []
    for i in range(N):
        if val_l[i] == 1:
            l.append(s_l[i])

    l.sort(reverse=True)
    #print(l)

    for i in range(len(l)):
        score, idx = l[i]
        if idx == N-1:
            if i < K:
                print("Yes")
            else:
                print("No")




if __name__ == '__main__':
    main()