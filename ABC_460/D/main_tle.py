import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    H = int(input_data[0])
    W = int(input_data[1])
    s_iter = iter(input_data[2:])
    S = []
    dot = 0
    for h in range(H):
        sn = next(s_iter)
        s_line = []
        for w in range(W):
            if sn[w] == ".":
                s_line.append(0)
                dot += 1
            else:
                s_line.append(1)
        S.append(s_line)
    #print(S)

    f1_s = []
    f2_dot = -1

    counter = 0
    anzen = 0
    while f2_dot != dot or counter % 2 == 1 or anzen <= 10:
        if f2_dot == dot:
            anzen += 1
        counter += 1
        #f2_dot
        if f1_s:
            f2_dot = 0
            for h in range(H):
                f2_dot += f1_s[h].count(0)
        f1_s = S
        #print(f2_s, f1_s)
        S = [[0 for _ in range(W)] for i in range(H)]
        #print(S)
        for h in range(H):
            for w in range(W):
                if f1_s[h][w] == 1:
                    if h != 0:
                        S[h-1][w] = 1
                    if h != H-1:
                        S[h+1][w] = 1
                    if w != 0:
                        S[h][w-1] = 1
                    if w != W-1:
                        S[h][w+1] = 1
                    if h != 0 and w != 0:
                        S[h-1][w-1] = 1
                    if h != 0 and w != W-1:
                        S[h-1][w+1] = 1
                    if h != H-1 and w != 0:
                        S[h+1][w-1] = 1
                    if h != H-1 and w != W-1:
                        S[h+1][w+1] = 1
        for h in range(H):
            for w in range(W):
                if f1_s[h][w] == 1:
                    S[h][w] = 0
        #print(S, counter)

        dot = 0
        for h in range(H):
            dot += S[h].count(0)


        """

        for h in range(H):
            ans = []
            for w in range(W):
                if S[h][w] == 0:
                    ans.append(".")
                else:
                    ans.append("#")
            print("".join(ans))
        print(f2_dot, dot, anzen)
        """

    for h in range(H):
        ans = []
        for w in range(W):
            if S[h][w] == 0:
                ans.append(".")
            else:
                ans.append("#")
        print("".join(ans))
    

if __name__ == '__main__':
    main()