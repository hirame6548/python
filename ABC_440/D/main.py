import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
import bisect

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    N = input_data[0]
    Q = input_data[1]

    c_iter = iter(input_data[2:])

    As = list(itertools.islice(c_iter, N))
    As.sort()
    #print(As)

    Cs = [As[i] - i for i in range(N)]
    #print(Cs)


    for _ in range(Q):
        X = next(c_iter)
        Y = next(c_iter)

        c_x = X - bisect.bisect_left(As, X)
        #print(c_x)
        c_y = c_x + Y - 1
        y = c_y + bisect.bisect(Cs, c_y)
        print(y)



if __name__ == '__main__':
    main()