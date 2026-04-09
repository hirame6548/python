M, D = map(int, input().split())

num_list = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]

default_answer = "No"
if (M, D) in num_list:
    default_answer = "Yes"

print(default_answer)