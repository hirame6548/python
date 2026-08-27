import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    S = input_data[0]

    f_s = ""
    frag = []
    for i in range(len(S)):
        if f_s == S[i]:
            frag.append(i)
        f_s = S[i]
    frag.append(len(S))
    #print(frag) # [2]

    ans = 0
    f_f = 0
    for f in frag:
        l = f - f_f
        ans += l + ((l*(l-1)) // 2)
        f_f = f

    print(ans % 998244353)
    

if __name__ == '__main__':
    main()