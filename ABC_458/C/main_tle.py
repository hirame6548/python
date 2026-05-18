import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    S = input_data[0]
    N = len(S)
    counter = 0

    for i in range(N):
        for j in range(i, N):
            if (j-i) % 2 == 1:
                continue
            else:
                c = (i+j) // 2
                if S[c] == "C":
                    counter += 1 
    
    print(counter)
    

if __name__ == '__main__':
    main()