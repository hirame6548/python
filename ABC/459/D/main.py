import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    T = int(input_data[0])
    case = iter(input_data[1:])
    c_d = defaultdict(int)

    for i in range(T):
        S = next(case)
        c_d.clear()
        max_c = 0
        for c in S:
            c_d[c] += 1
            if c_d[c] > max_c:
                max_c = c_d[c]
                char = c
        l = len(S)
        if l - max_c + 1 >= max_c:
            ans = []
            frag = True
            for j in S:
                if max_c and frag:
                    ans.append(char)
                    max_c -= 1
                    frag = False
                if j != char:
                    frag = True
                    ans.append(j)
            if max_c:
                ans.append(char)
            print("Yes")
            print("".join(ans))
        else:
            print("No")

if __name__ == '__main__':
    main()