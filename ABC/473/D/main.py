import sys
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, accumulate
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(10**6)

# Trueの間はテストが失敗する。提出前にFalseへ変更する
DEBUG = 0

if DEBUG:
    print("[DEBUG MODE]", file=sys.stderr)


def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)


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
        n = N + 1 - length
        n_max = rest // n
        generated = [
            [in_l[0] - n * i] + in_l[1:] + [i]
            for i in range(n_max + 1)
        ]
        debug("generated:", generated)
        return generated

    stack = [[K]]
    ans = []

    while stack:
        current = stack.pop()
        debug("pop:", current, "stack_size:", len(stack))

        if len(current) == N:
            current.append(current[0])
            answer = list(reversed(current[1:]))
            ans.append(answer)
            debug("answer:", answer, "answer_count:", len(ans))
        else:
            stack += rec(N, current)

    ans.sort()
    for answer in ans:
        print(*answer)


if __name__ == "__main__":
    main()
