S = input()

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ans = []
for s in S:
    if s in num_list:
        ans.append(s)

print("".join(ans))
