H, W = map(int, input().split())

Ss = []
for i in range(H):
    Ss.append(input())

Ss.insert(0, "#" * W)
Ss.append("#" * W)

for i in range(H+2):
    Ss[i] = "#" + Ss[i] + "#"
    if "S" in set(Ss[i]):
        S_xy = (i, Ss[i].index("S"))


src = []
cur = S_xy

from collections import deque

