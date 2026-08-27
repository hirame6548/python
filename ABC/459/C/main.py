import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    N = input_data[0]
    Q = input_data[1]
    
    q_iter = iter(input_data[2:])
    v_l = [0]*N
    num_l = [N] + ([0] * (Q))
    counter = 0

    max_v = 0

    for i in range(Q):
        q = next(q_iter)
        x = next(q_iter)

        if q == 1:
            v = v_l[x-1]
            num_l[v] -= 1
            num_l[v+1] += 1
            v_l[x-1] += 1
            if v_l[x-1] > max_v:
                max_v = v_l[x-1]
            if num_l[0] == 0:
                counter += 1
                num_l.pop(0)

        if q == 2:
            ans = 0
            for i in range(x, max_v+1):
                ans += num_l[i]
            print(ans)

        #print(q, v_l, num_l, counter)

if __name__ == '__main__':
    main()