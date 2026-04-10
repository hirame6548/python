import sys
Q = int(input())

height = []

for line in sys.stdin:
    d, h = map(int, line.split())
    height.append(h)
    if d == 2:
        height.append(0)
        for i in range(len(height)):
            if height[i] <= h:
                height[i] = 0
    print(len(height) - height.count(0))