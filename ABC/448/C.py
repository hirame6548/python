N, Q = map(int, input().split())

As = list(map(int, input().split()))

fix_As = [x for x in As]

import heapq

As = [(As[i], i) for i in range(N)]

#As.sort() # [(1, 4), (2, 1), (2, 5), (3, 0), (5, 2), (9, 3)]
heap = [x for x in As]
heapq.heapify(heap)

h_v = [heapq.heappop(heap) for _ in range(N)] # [(1, 4), (2, 1), (2, 5), (3, 0), (5, 2), (9, 3)]

heap = [x for x in As]
heapq.heapify(heap)
h_i = {heapq.heappop(heap)[1] : i for i in range(N)}
#print(h_i)

for i in range(Q):
    K = int(input())
    q = list(map(lambda x: h_i[int(x)-1], input().split()))
    s_q = set(q)
    min = 0
    for j in range(K):
        if min in s_q:
            min += 1
        else:
            break
    #print(q, min, s[min], fix_As)
    #print(c_As)
    ans = h_v[min][0]
    #ans = fix_As[ans[0]]
    print(ans)