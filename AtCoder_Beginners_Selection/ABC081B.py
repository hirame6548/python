N = int(input())

As = list(map(int, input().split()))

cs = []
for i in range(N):
    c = 0
    while As[i] % 2 == 0:
        As[i] = As[i] / 2
        c += 1
    cs.append(c)

print(min(cs))