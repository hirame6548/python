N = int(input())

C_list = [[0 for _ in range(N+5)] for _ in range(N+5)]

row_list = []
for i in range(N-1):
    row_list = list(map(int, input().split()))
    #print(row_list)
    for j in range(len(row_list)):
        C_list[i+1][i+j+2] = row_list[j]
        #print(C_list, i, j)
        

judge = False
for i in range(1, N+1):
    for j in range(i+2, N+3):
        for k in range(i+1, j):
            #print(i, k, j, C_list[i][k] + C_list[k][j], C_list[i][j])
            if C_list[i][k] + C_list[k][j] < C_list[i][j]:
                judge = True
                break
        if judge:
            break
    if judge:
        break

if judge:
    print("Yes")
else:
    print("No")