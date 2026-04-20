N, M = map(int, input().split())

A_B = []

for i in range(M):
    a_b = tuple(map(int, input().split()))
    A_B.append(a_b)

tugi = [set() for _ in range(N)] # [{2}, {3, 4}, {4}, set(), {2}]
#print(tugi)
for a, b in A_B:
    tugi[a-1].add(b)


visited = set([1])
plus = set([1])
for _ in range(N):
    ad = set()
    for i in plus:
        ad.update(tugi[i-1])
    #print(visited, ad, ad - visited)
    plus = ad - visited
    #print(plus)
    if not plus:
        break
    else:
        visited.update(plus)

print(len(visited))