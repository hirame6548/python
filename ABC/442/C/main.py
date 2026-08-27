import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from scipy.special import comb

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])

    ab_iter = map(int, input_data[2:])
    
    counter = [0] * N
    #print(counter)

    for ab in ab_iter:
        counter[ab-1] += 1
    #print(counter)

    ans = []
    for c in counter:
        rest = N - c - 1
        if rest <= 2:
            ans.append(0)
        else:
            ans.append(comb(rest, 3, exact=True))
    
    print(*ans)


if __name__ == '__main__':
    main()