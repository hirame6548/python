N, X = map(int, input().split())

As = list(map(int, input().split()))

for i in range(N):
    if As[i] < X:
        X = As[i]
        print("1")
    else:
        print("0")