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
    #print(N, A)

    # ---------- solve ----------
    a_set = set()
    for i in range(N):
        a = next(it)
        if a in a_set:
            a_set.remove(a)
        else:
            a_set.add(a)

    print(sum(a_set))





if __name__ == "__main__":
    main()