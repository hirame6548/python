Q = int(input())

dirc = []
height = []

for i in range(Q):
    d, h = list(map(int, input().split()))
    dirc.append(d)
    height.append(h)

counter = []

for i in range(Q):
    if dirc[i] == 1:
        counter.append(height[i])
    else:
        counter.append(0)
        for j in range(i):
            if counter[j] <= height[i]:
                counter[j] = 0
    print(len(counter) - counter.count(0))