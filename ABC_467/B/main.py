import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    abs = iter(input_data[1:])

    ans = 0
    for i in range(N):
        A = int(next(abs))
        B = int(next(abs))
        S = next(abs)

        if S == "keep":
            ans += B-A
    
    print(ans)
    

if __name__ == '__main__':
    main()