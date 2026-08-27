N = int(input())

max_num = 10**9

int_list = [] # [1, 2, 4, 8, 16, 32, 64, ...

val_num = 1
while val_num <= max_num:
    int_list.append(val_num)
    val_num *= 2

int_str = list(map(str, int_list)) # ['1', '2', '4', '8', '16', '32', '64', ...
int_dig = list(map(len, int_str)) # [1, 1, 1, 1, 2, 2, ...


int_dig_list = [] # [['1', '2', '4', '8'], ['16', '32', '64'], ['128', ...

for i in range(9):
    int_dig_list.append([j for j in int_str if len(j) == i +1])
    

# 入力：dig = 生成したい桁数, list = 生成元のリストのリスト(文字列！)
# 出力：list の数字を組み合わせてできる dig 桁の数字のリスト

def num_generator(dig, list, int_dig_list):
    num_set = set(int_dig_list[dig - 1]) # dig = 2, {'64', '16', '32'}
    for i in range(dig - 1):
        x_list = list[i]
        y_list = int_dig_list[dig - i - 2]
        for j in range(len(x_list)):
            for k in range(len(y_list)):
                new_num = x_list[j] + y_list[k]
                if not new_num in num_set:
                    num_set.add(new_num)
    dig_list = sorted(num_set)
    return dig_list # dig = 2, ['11', '12', '14', '16', '18', '21', '22', '24', '28', '32', '41', '42', '44', '48', '64', '81', '82', '84', '88']


cur_dig_list = int_dig_list.copy()
for i in range(8):
    cur_dig_list[i+1] = num_generator(i+2, cur_dig_list, int_dig_list) #2桁目からしかいらない, 9桁目まで

num_of_list = list(map(len, cur_dig_list)) # [4, 19, 89, 421, 1989, 9399, 44413, 209865, 991675]

val_num = N
counter = 0
while val_num - num_of_list[counter] > 0:
    val_num -= num_of_list[counter]
    counter += 1

answer = cur_dig_list[counter][val_num - 1]

print(answer)