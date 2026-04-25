N = int(input())
S = input()

ans = ""
frag = 1
for i in range(N):
    if S[i] != "o":
        ans += S[i]
        frag = 0
    elif frag == 0:
        ans += S[i]
        


print(ans)