N, M = map(int, input().split())

Cs = list(map(int, input().split()))

As = []
Bs = []

for i in range(N):
    a, b = map(int, input().split())
    As.append(a)
    Bs.append(b)

sums = [0] * M
for i in range(N):
    sums[As[i]-1] += Bs[i]

for i in range(M):
    if sums[i] > Cs[i]:
        sums[i] = Cs[i]


print(sum(sums))