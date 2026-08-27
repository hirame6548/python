import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    T = int(input_data[0])
    case_iter = iter(input_data[1:])


    for _ in range(T):
        N = int(next(case_iter))
        C = int(next(case_iter))
        S = []
        for i in range(N):
            S.append("#" + next(case_iter) + "#")
        #print(N, C, S)

        drc = [(-1, -1), (-1, 0), (-1, 1)]
        ans = [0 * N]
        for i in range(N):
            cur = (N, C)
            for d in drc:
                nxt = cur + drc






if __name__ == '__main__':
    main()