import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    S_iter = iter(input_data[1:])

    ans = []

    list_2 = ["a", "b", "c"]
    list_3 = ["d", "e", "f"]
    list_4 = ["g", "h", "i"]
    list_5 = ["j", "k", "l"]
    list_6 = ["m", "n", "o"]
    list_7 = ["p", "q", "r", "s"]
    list_8 = ["t", "u", "v"]
    list_9 = ["w", "x", "y", "z"]

    for i in range(N):
        S = next(S_iter)
        if S[0] in list_2:
            ans.append("2")
        if S[0] in list_3:
            ans.append("3")
        if S[0] in list_4:
            ans.append("4")
        if S[0] in list_5:
            ans.append("5")
        if S[0] in list_6:
            ans.append("6")
        if S[0] in list_7:
            ans.append("7")
        if S[0] in list_8:
            ans.append("8")
        if S[0] in list_9:
            ans.append("9")

    print("".join(ans))
    
    

if __name__ == '__main__':
    main()