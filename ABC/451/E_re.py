N = int(input()) # 4

A_list = [[0] * (N+1) for _ in range(N+1)] # [[0, 0, 0, 0, 0], [0, 0, 2, 5, 4], [0, 0, 0, 3, 2], [0, 0, 0, 0, 5], [0, 0, 0, 0, 0]]

for i in range(1, N):
    A_list[i][i+1:N+1] = list(map(int, input().split()))


# 入力：3つの数
# 出力：任意の数が残り２つの和を超えたら False, そうでなければ True を返す 
def num_judge(n_1, n_2, n_3):
    if n_1 > n_2 + n_3:
        return False
    if n_2 > n_3 + n_1:
        return False
    if n_3 > n_1 + n_2:
        return False
    return True


index_list = [] # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
for i in range(1, N):
    for j in range(i+1, N+1):
        index_list.append((i, j))


output = "Yes" # "Yes" or "No"
for x, y in index_list:
    for i in range(y+1, N+1): # i = y+1, y+2, ... N
        judge = num_judge(A_list[x][y], A_list[x][i], A_list[y][i])
        if not judge:
            output = "No"
            break
    if not judge:
        break

print(output)