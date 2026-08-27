import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])
    As = list(map(int, input_data[2:N+2]))
    Bs = list(map(int, input_data[N+2:2*N+1]))

    b_n = 0
    for i in range(N-1):
        b_n = (-b_n - Bs[i]) % M
        As[i+1] = (As[i+1] + b_n) % M



    print(As)
    
    

if __name__ == '__main__':
    main()