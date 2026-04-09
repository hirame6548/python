S = input() # rdddrdtdcdrrdcredctdordoeecrotet
T = input() # dcre

t_0_list = [i for i, x in enumerate(S) if x == T[0]]
#print(t_0_list) # [1, 2, 3, 5, 7, 9, 12, 16, 19, 22]

i_list = []
src_ind = 0
counter = 0

for i in range(len(t_0_list)):
    src_ind = t_0_list[i]
    counter = 1
    last_ind = src_ind
    while counter < len(T) and src_ind < len(S)-1:
        src_ind += 1
        #print(src_ind, counter)
        if S[src_ind] == T[counter]:
            last_ind = src_ind
            counter += 1
    if counter == len(T):
        i_list.append([t_0_list[i], last_ind])

#print(i_list) # [[1, 15], [2, 15], [3, 15], [5, 15], [7, 15], [9, 15], [12, 15], [16, 24], [19, 30], [22, 30]]


i_min_list = []

for i in range(len(i_list)):
    if i == len(i_list) - 1:
        i_min_list.append(i_list[i])
        continue
    elif i_list[i][1] < i_list[i+1][1]:
        i_min_list.append(i_list[i])

#print(i_min_list) # [[12, 15], [16, 24], [22, 30]]


def counting(len_list, src_len):
    f, l = len_list
    f_s, l_s = src_len
    return (f - f_s + 1) * (l_s - l + 1)


minus = 0
src_len = [0, len(S)-1]

for i in range(len(i_min_list)):
    #print("A_1", minus, counting(i_min_list[i], search_len), i_min_list[i], search_len)
    minus += counting(i_min_list[i], src_len)
    src_len[0] = i_min_list[i][0] + 1


sum_pattern = int(((len(S) + 1) * len(S)) / 2)

print(sum_pattern - minus)