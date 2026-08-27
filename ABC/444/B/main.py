N, K = map(int, input().split())
#print(N, K)


counter = 0
for i in range(1, N+1):
    digit_list = []
    #print(i)
    while i >= 1:
        digit_list.append(i % 10)
        i = i // 10
        #print(digit_list)
    dig_sum = sum(digit_list)
    if dig_sum == K:
        counter += 1

print(counter)