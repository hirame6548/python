import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    Q = int(input_data[1])
    As = list(map(int, input_data[2:N+2]))
    q_iter = map(int, input_data[N+2:])

    a_sum = 0
    for i in range(N):
        a_sum += As[i]
        As[i] = a_sum
    As.insert(0, 0)
    #print(As)

    
    for _ in range(Q):
        q = next(q_iter)
        if q == 1:
            i = next(q_iter)
            As[i] = As[i-1] + (As[i+1] - As[i])
        else:
            l = next(q_iter) - 1
            r = next(q_iter)
            print(As[r] - As[l])



if __name__ == '__main__':
    main()