H, W = list(map(int, input().split()))


matrix = [[0 for i in range(W)] for _ in range(H)]


counter = 0
ran_list = []
frag_list = [0]
for i in range(H):
    len_cnt = 0
    start_j = 0
    in_str = input()
    edit_str = "#" + in_str + "#"
    for j in range(W):
        if edit_str[j+1] == ".":
            len_cnt += 1
            if edit_str[j] == "#":
                counter += 1
                matrix[i][j] = counter
                start_j = j
                if i == 0 or i == H-1 or j == 0 or j == W-1:
                    frag_list.append(0)
                else:
                    frag_list.append(1)
            else:
                matrix[i][j] = counter
            if edit_str[j+2] == "#":
                ran_list.append((i, range(start_j, start_j + len_cnt)))
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                frag_list[counter] = 0
        else:
            len_cnt = 0

cnt_list = [i for i in range(len(frag_list))]

for i in range(len(ran_list)):
    num = 0
    if ran_list[i][0] == 0:
        continue
    else:
        for j in ran_list[i][1]:
            #print(ran_list[i][1], i, j, matrix[ran_list[i][0]-1])
            if matrix[ran_list[i][0]-1][j] != 0:
                num = matrix[ran_list[i][0]-1][j]
                break
                #print("num=", num)
        for j in ran_list[i][1]:
            if matrix[ran_list[i][0]-1][j] != 0 and matrix[ran_list[i][0]-1][j] != num:
                if frag_list[matrix[ran_list[i][0]-1][j]] == 0:
                    frag_list[num] = 0
                cnt_list[matrix[ran_list[i][0]-1][j]] = 0
    if num:
        cnt_list[matrix[ran_list[i][0]][ran_list[i][1][0]]] = 0
        for j in ran_list[i][1]:
            matrix[ran_list[i][0]][j] = num
        frag_list[num] = min(frag_list[num], frag_list[i+1])


#print(cnt_list)

#ran_list = [(1, range(4, 5)), (2, range(3, 6)), (3, range(2, 3)), (3, range(6, 7)), (3, range(9, 14)), (4, range(2, 7)), (4, range(9, 10)), (4, range(14, 15)), (5, range(0, 1)), (5, range(7, 8)), (5, range(9, 15)), (5, range(16, 21)), (6, range(0, 1)), (6, range(7, 8)), (6, range(9, 10)), (6, range(14, 15)), (6, range(16, 17)), (7, range(9, 14)), (7, range(16, 17)), (8, range(16, 17)), (9, range(16, 21))]
#print("frag=",frag_list)
#for i in range(H):
    #print(matrix[i])

ans = 0
for i in cnt_list:
    ans += frag_list[i]

print(ans)