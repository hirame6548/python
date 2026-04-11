T, X = map(int, input().split())

As = list(map(int, input().split()))

print(0, As[0])
pre_A = As[0]
for i in range(1, T+1):
    if abs(As[i] - pre_A) >= X:
        print(i, As[i])
        pre_A = As[i]
