H, W, Q = list(map(int, input().split()))


for i in range(Q):
    q, l = list(map(int, input().split()))
    if q == 1:
        H = H - l
        print(l * W)
    else:
        W = W - l
        print(H*l)

