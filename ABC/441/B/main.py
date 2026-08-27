import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])
    
    S = input_data[2]
    T = input_data[3]

    Q = int(input_data[4])

    ws = input_data[5:]

    s_set = set()
    for i in range(N):
        s_set.add(S[i])
    t_set = set()
    for i in range(M):
        t_set.add(T[i])
    #print(s_set, t_set)
    
    for w in ws:
        l = len(w)
        t = True
        a = True
        for i in range(l):
            if not w[i] in s_set:
                t = False
            if not w[i] in t_set:
                a = False
        if t and not a:
            print("Takahashi")
        elif a and not t:
            print("Aoki")
        else:
            print("Unknown")




if __name__ == '__main__':
    main()