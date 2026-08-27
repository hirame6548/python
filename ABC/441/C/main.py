import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    K = int(input_data[1])
    X = int(input_data[2])

    As = list(map(int, input_data[3:]))
    As.sort()
    #print(As)

    sum = 0
    for i in range(K-1, -1, -1):
        sum += As[i]
        drunk = -1
        if sum >= X:
            drunk = i
            break
    
    if drunk == -1:
        print("-1")
    else:
        print(N - drunk)
    

if __name__ == '__main__':
    main()