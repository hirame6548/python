import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    T = int(input_data[0])
    case_iter = iter(list(map(int, input_data[1:])))

    for _ in range(T):
        N = next(case_iter)
        case = []
        for i in range(N):
            case.append(next(case_iter))
        #print(Ns, cases)

        ans = 0
        f_c = N
        for i in range(len(case)):
            if case[i] - f_c > 1:
                ans += case[i] - (f_c + 1)
                case[i] = f_c + 1
            f_c = case[i]

        case.reverse()
        f_c = N
        for i in range(len(case)):
            if case[i] - f_c > 1:
                ans += case[i] - (f_c + 1)
                case[i] = f_c + 1
            f_c = case[i]
        print(ans)


if __name__ == '__main__':
    main()