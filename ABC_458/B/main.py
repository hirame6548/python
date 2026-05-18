import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    H = int(input_data[0])
    W = int(input_data[1])
    
    for h in range(H):
        l = []
        for w in range(W):
            a = 4
            if h == 0:
                a -= 1
            if h == H-1:
                a -= 1
            if w == 0:
                a -= 1
            if w == W-1:
                a -= 1
            l.append(a)
        print(*l)


if __name__ == '__main__':
    main()