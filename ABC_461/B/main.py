import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    A = list(map(int, input_data[1:N+1]))
    B = list(map(int, input_data[N+1:]))
    #print(A, B)

    a_b = [0 for _ in range(N)]
    #print(a_b)

    frag = True
    for i in range(N):
        ono_n = A[i] - 1
        if B[ono_n] - 1 == i:
            continue
        else:
            frag = False
            break
    
    if frag:
        print("Yes")
    else:
        print("No")
    
    

if __name__ == '__main__':
    main()