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

    t = {"A":0, "B":1, "C":2, "D":3, "E":4}

    N = int(next(it))
    X = t[next(it)]
    S = [next(it) for _ in range(N)]

    is_no = True
    for i in range(N):
        if S[i][X] == "o":
            print("Yes")
            is_no = False
            break

    if is_no:
        print("No")

if __name__ == '__main__':
    main()