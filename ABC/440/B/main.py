N = int(input())

Ts = list(map(int, input().split()))

T_idx = []
for i, x in enumerate(Ts):
    T_idx.append((x, i))
T_idx.sort()

ans = []
for i in range(3):
    ans.append(T_idx[i][1]+1)

print(*ans)