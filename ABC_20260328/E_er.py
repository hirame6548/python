N = int(input()) # 4


A_list = [] # [[2, 5, 4], [3, 2], [5]]
for i in range(N-1):
    A_list.append(list(map(int, input().split())))

edit_A_list = A_list # [[0, 0, 0, 0, 0], [0, 2, 5, 4], [0, 3, 2], [0, 5], [0]]
edit_A_list.append([])
for i in range(N):
    edit_A_list[i].insert(0, 0)

zero_list = []
for i in range(N+1):
    zero_list.append(0)
edit_A_list.insert(0, zero_list)

#print(edit_A_list)

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

# 出力：A_xy
def edit_index(x, y, num_list):
    return num_list[x][y-x]


output = "Yes" # "Yes" or "No"
for x, y in index_list:
    for i in range(y+1, N+1): # i = y+1, y+2, ... N
        #print(x, y, i)
        #print(edit_index(x, y, edit_A_list), edit_index(x, i, edit_A_list), edit_index(y, i, edit_A_list))
        judge = num_judge(edit_index(x, y, edit_A_list), edit_index(x, i, edit_A_list), edit_index(y, i, edit_A_list))
        #print(judge)
        if not judge:
            output = "No"
            break
    if not judge:
        break

print(output)