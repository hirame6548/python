N = int(input())

max_num = 10**9

int_list = []

val_num = 1
while val_num <= max_num:
    int_list.append(val_num)
    val_num *= 2

# int_list は初期値のリストとする、追加はしない

int_str_list = list(map(str, int_list))
int_dig_list = list(map(len, int_str_list)) #[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9]


dig_list = []
length_list = []
dig_cur_list = []
dig_set = []


# 文字型のリスト
dig_1_list = [i for i in int_str_list if len(i) == 1]
dig_list.append(dig_1_list)


length_1 = len(dig_1_list)
length_list.append(length_1)

dig_1_set = set(dig_1_list)
dig_set.append(dig_1_set)

dig_2_list = [i for i in int_str_list if len(i) == 2]

dig_2_set = set(dig_2_list)
dig_set.append(dig_2_set)

for i in range(length_1):
    for j in range(length_1):
        dig_2_str = dig_1_list[i] + dig_1_list[j]
        if not dig_2_str in dig_2_set:
            dig_2_set.add(dig_2_str)

dig_2_list = sorted(dig_2_set)
dig_list.append(dig_2_list)

length_2 = len(dig_2_list)
length_list.append(length_2)




dig_3_list = [i for i in int_str_list if len(i) == 3]

dig_3_set = set(dig_3_list)
dig_set.append(dig_3_set)

for i in range(length_2):
    for j in range(length_2):
        dig_3_str = dig_2_list[i] + dig_2_list[j]
        if not dig_3_str in dig_3_set:
            dig_3_set.add(dig_3_str)

dig_3_list = sorted(dig_3_set)
dig_list.append(dig_3_list)

length_3 = len(dig_3_list)
length_list.append(length_3)

for i in range(9):
    i_dig_list = [j for j in int_str_list if len(j) == i + 1]
    dig_cur_list.append(i_dig_list)

"""
dig_cur_list
dig_set
dig_list
length_list
"""

# 入力：上の４つ
# 出力：上の４つ
def operation(dig_cur_list, dig_set, dig_list, length_list):
    dig_set.append()