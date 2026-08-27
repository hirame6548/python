N, K = map(int, input().split())
#print(N, K)

counter = 0
mame = N
while mame < K:
    N += 1
    mame += N
    counter += 1
    #print(mame, N, counter)

print(counter)