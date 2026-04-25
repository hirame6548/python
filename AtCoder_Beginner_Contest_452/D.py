import heapq
import copy

S = input() # abrakadabra
T = input() # aba

S_index_list = [] # [[0, 3, 5, 7, 10], [1, 8], [0, 3, 5, 7, 10]]
for i in range(len(T)): # i = 0, 1, 2
    S_index_list.append([j for j, x in enumerate(S) if x == T[i]])

for i in range(len(T)):
    S_index_list[i] = list(S_index_list[i])


"""
l_t = len(T) # 3
for l in range(1, len(S)+1):
    print(l)
    for i in range(len(S_index_list[0])):
        print(i, S_index_list[0][i], S_index_list[0][i]+l)
        i_set = set(range(S_index_list[0][i], S_index_list[0][i]+l))
        print(i_set) # {0, 1, 2, 3, 4, 5, 6} (l = 7, i = 0)
        for i_t in range(l_t):
"""

min_i_list = [] # [[0, 1, 3], [3, 8, 10], [5, 8, 10], [7, 8, 10]]
index_num = len(S_index_list[0])

for i in range(index_num): # i = 0, 1, 2, 3, 4
    num_list = []
    num_list.append(S_index_list[0][i])
    for l in range(1, len(S_index_list)): # l = 1, 2
        length = len(S_index_list[l]) # l文字目の要素数
        for j in range(length):
            if num_list[-1] >= S_index_list[l][j]:
                continue
            else:
                num_list.append(S_index_list[l][j])
                #print(num_list)
                break
    if len(num_list) == len(S_index_list):
        min_i_list.append(num_list)

#print(min_i_list)

min_len_list =[] # [[0, 3], [7, 10]]
min_i_list_len = len(min_i_list)
for i in range(min_i_list_len):
    judge = True
    for j in range(i, min_i_list_len):
        if i != j and min_i_list[i][0] <= min_i_list[j][0] and min_i_list[i][-1] >= min_i_list[j][-1]:
            judge = False
            break
    if judge:
        min_len_list.append([min_i_list[i][0], min_i_list[i][-1]])

def counting(len_list, whole_len):
    #print(len_list, whole_len)
    f, l = len_list
    sum = 0
    for i in range(whole_len - (l-f)):
        #print(i, min(l+i, whole_len) - max(f-i, 0) - i - (l-f) + 1)
        sum += min(l+i, whole_len-1) - max(f-i, 0) - i - (l-f) + 1
        #print(sum)
    return sum



s_len = len(S) # 11
s_len_fix = copy.copy(s_len)
m_l_len = len(min_len_list)
min_len_list_fix = copy.copy(min_len_list)
minus = 0
for i in range(m_l_len):
    #print(i, minus)
    minus += counting(min_len_list[i], s_len)
    #print(min_len_list[i], s_len, minus)
    try:
        s_len -= min_len_list[i][0] + 1
        min_len_list[i+1] = [min_len_list_fix[i+1][0] - min_len_list_fix[i][0] - 1, min_len_list_fix[i+1][1] - min_len_list_fix[i][0]-1]
    except:
        #print("End")
        continue

#print(min_len_list, min_len_list_fix)


sum_pattern = ((s_len_fix + 1) * s_len_fix) / 2

#print(s_len_fix, sum_pattern)
#print(min_len_list)
print(int(sum_pattern - minus))