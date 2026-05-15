import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    A = list(map(int, input_data[1:1+N]))

    X = int(input_data[1+N])

    print(A[X-1])
    
    

if __name__ == '__main__':
    main()