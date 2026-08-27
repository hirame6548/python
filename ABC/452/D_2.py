S = input() # abrakadabra
T = input() # aba

count = 0
i_list = [] # [[0, 1, 3], [5, 8, 10]]
#print(i_list)

test_str = [-1 for _ in range(len(T))] # [-1, -1, -1]


#print(test_str)
#print(T[0])
#print(test_str[0])

str_set = set(T)
for i in range(len(S)):
    if S[i] in str_set:
        if S[i] == T[test_str.index(-1)]:
            #print(test_str.index(-1))
            test_str[test_str.index(-1)] = i
            if test_str[-1] != -1:
                i_list.append(test_str)
                test_str = [-1 for _ in range(len(T))]
    else:
        continue

test_str = [-1 for _ in range(len(T))]

i_min_list = []
for i in range(len(i_list)):
    for j in range(i_list[i][-1], -1, -1):
        #print(j, S[j], test_str.index(-1))
        if S[j] == T[len(T) -1 - test_str.index(-1)]:
            test_str[test_str.index(-1)] = j
            if test_str[-1] != -1:
                i_min_list.append(test_str)
                test_str = [-1 for _ in range(len(T))]
                break

range_list =[]
for i in range(len(i_min_list)):
    range_list.append([i_min_list[i][-1], i_min_list[i][0]])

print(range_list) # [[0, 3], [7, 10]]


def counting(len_list, whole_len):
    f, l = len_list
    return (f + 1) * (whole_len - l)

minus = 0
search_len = len(S)

for i in range(len(range_list)):
    print("A_1", minus, counting(range_list[i], search_len), range_list[i], search_len)
    minus += counting(range_list[i], search_len)
    move_len = range_list[i][0] + 1
    search_len -= move_len
    print("A_2", minus, counting(range_list[i], search_len), range_list[i], search_len)
    for j in range(i, len(range_list)):
        range_list[j][0] -= move_len
        range_list[j][1] -= move_len
        print("B", j, range_list[j][0], range_list[j][1], search_len)

sum_pattern = int(((len(S) + 1) * len(S)) / 2)

print(sum_pattern - minus)