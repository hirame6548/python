N, M = input().split()
N = int(N)
M = int(M)

num_list = []
for i in range(N):
    num_list.append(input().split())

# 入力した数値は文字列

this_year = []
next_year = []
for i in range(N):
    this_year.append(num_list[i][0])
    next_year.append(num_list[i][1])

this_year_list = []
next_year_list = []
for i in range(M):
    this_year_list.append(this_year.count(f"{i+1}"))
    next_year_list.append(next_year.count(f"{i+1}"))

for i in range(M):
    print(next_year_list[i] - this_year_list[i])