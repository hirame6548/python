N, K = list(map(int, input().split())) # 3 10
As = list(map(int, input().split())) # [3, 21, 9]
r_As = list(map(lambda x: x%K , As))
r_As.sort()

min_gap = r_As[-1] - r_As[0]
for i in range(N-1):
    min_gap = min(min_gap, r_As[i]+K - r_As[i+1])

print(min_gap)
