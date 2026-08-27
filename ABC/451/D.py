N = int(input())

n = 1
n_list = [] #['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432', '67108864', '134217728', '268435456', '536870912']
max_num = 10**9
max_digit = 8
while n <= max_num:
    n_list.append(n)
    n *= 2

n_str_list = list(map(str, n_list))

n_digit_list = [] #[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9]
for i in range(len(n_str_list)):
    n_digit_list.append(len(n_str_list[i]))

n_number_fixed = len(n_list)
n_number = len(n_list)


for _ in range(max_digit - 1):
    n_number = len(n_list)
    for i in range(n_number):
        for j in range(n_number_fixed):
            n_list.append(n_list[i] + n_list[j] * 10**len(str(n_list[i])))
    n_list = [i for i in n_list if i <= max_num]

sorted_list = sorted(set(n_list))

print(sorted_list[N-1])