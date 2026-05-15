import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    N = int(input_data[0])
    
    int_iter = iter(input_data[1:])

    As = []

    for i in range(N):
        L = next(int_iter)
        A = list(itertools.islice(int_iter, L))
        As.append(A)

    X = next(int_iter)
    Y = next(int_iter)

    print(As[X-1][Y-1])
    
    

if __name__ == '__main__':
    main()