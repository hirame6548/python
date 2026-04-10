N = int(input()) # 4

A_list = [[0] * (N+1) for _ in range(N+1)] # [[0, 0, 0, 0, 0], [0, 0, 2, 5, 4], [0, 0, 0, 3, 2], [0, 0, 0, 0, 5], [0, 0, 0, 0, 0]]

for i in range(1, N):
    A_list[i][i+1:N+1] = list(map(int, input().split()))


"""
min_num = 9999
for i in range(len(A_list)):
    for j in range(len(A_list[i])):
        if not A_list[i][j] == 0 and A_list[i][j] <= min_num:
            min_num = A_list[i][j]

print(min_num)
"""

min_num = min(((val, x, y) for x, row in enumerate(A_list) for y, val in enumerate(row) if val > 0), default = None)

