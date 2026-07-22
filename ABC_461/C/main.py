import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])

    CV_iter = map(int, input_data[3:])

    CV = []
    for i in range(N):
        c = next(CV_iter)
        v = next(CV_iter)
        CV.append((v, c))
    CV.sort(reverse=True)
    CV = deque(CV)
    #print(CV)

    c_set = set()
    ans = 0
    rest_n = M

    for i in range(K):
        print(i)
        v, c = CV.popleft()
        if not c in c_set:
            rest_n -= 1
            c_set.add(c)
            ans += v
            print(ans)
        else:
            ans += v
            print(ans)
        if rest_n + (i+1) == M:
            break
    
    if rest_n > 0:
        while rest_n:
            v, c = CV.popleft()
            if not c in c_set:
                rest_n -= 1
                c_set.add(c)
                ans += v


    print(ans)
    

if __name__ == '__main__':
    main()