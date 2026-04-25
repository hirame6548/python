N, M = map(int, input().split())

A_B = []

for i in range(M):
    a_b = tuple(map(int, input().split()))
    A_B.append(a_b)

A_B = set(A_B)


visited = set([1])

for i in range(N):
    ad = set()
    sb = set()
    for a, b in A_B:
        #print("a, b", a, b)
        if a in visited and not b in visited:
            ad.add(b)
            sb.add((a, b))
    if not ad:
        break
    visited.update(ad)
    A_B -= sb



print(len(visited))
