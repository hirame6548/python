N, M = map(int, input().split())

Fs = list(map(int, input().split()))

F_l = []

Frag = True
for i in range(N):
    if Fs[i] in F_l:
        print("No")
        Frag = False
        break
    else:
        F_l.append(Fs[i])

if Frag:
    print("Yes")


if set(Fs) == set(range(1, M+1)):
    print("Yes")
else:
    print("No")

