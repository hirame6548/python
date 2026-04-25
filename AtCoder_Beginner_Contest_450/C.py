H, W = list(map(int, input().split()))

dp = []
dp_set = set()
frag = 0
counter = 0
len_count = 0
ran_list = []
for i in range(H):
    in_str = input()
    len_count = 0
    start_num = -1
    ran_list = []
    for j in range(W):
        #print(j, len_count)
        if in_str[j] == "." and j == 0:
            start_num = j
            len_count += 1
        elif in_str[j] == "." and in_str[j-1] == "#":
            start_num = j
            len_count += 1
        elif in_str[j] == "." and j == W-1:
            len_count += 1
            ran_list.append(range(start_num, start_num + len_count))
            len_count == 0
        elif in_str[j] == ".":
            len_count += 1
        elif in_str[j] == "#" and in_str[j-1] == ".":
            len_count == 0
            ran_list.append(range(start_num, start_num + len_count))
        else:
            len_count = 0

    for j in range(len(ran_list)):
        if set(ran_list[j]) & dp_set:
            continue
        elif i == 0:
            continue
        else:
            counter += 1

    if i == 0 or i == H-1:
        frag = 0
    else:
        frag = 1
    if dp_set:
        continue
    else:
        counter += frag


    dp_set = set([j for j, x in enumerate(in_str) if x == "."])
    dp = ran_list





