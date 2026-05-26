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

    v_d = defaultdict(int)
    v_d[0] = N
    v_l = [0] * N
    counter = 0
    max_v = 0

    for i in range(Q):
        q = next(q_iter)
        x = next(q_iter)
        if q == 1:
            v_l[x-1] += 1
            if v_l[x-1] > max_v:
                max_v = v_l[x-1]
            v_d[v_l[x-1]-1] -= 1
            v_d[v_l[x-1]] += 1
            if v_d[0] == 0:
                max_v -= 1
                for j in range(N):
                    v_l[j] -= 1
                for k in range(max_v+1):
                    #print("k", k)
                    v_d[k] = v_d[k+1]
            #print(q, v_l, v_d)
        else:
            ans = 0
            for k in range(max_v+1):
                #print("k", k)
                if k >= x:
                    ans += v_d[k]
            print(ans)



if __name__ == '__main__':
    main()