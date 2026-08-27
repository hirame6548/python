import heapq

import sys
Q = int(input())

# 空リストはすでに heap であり、 heapify は必要ない
heap = []

for line in sys.stdin:
    d, h = map(int, line.split())
    if d == 1:
        heapq.heappush(heap, h)
    else:
        while heap and heap[0] <= h:
            min_heap = heapq.heappop(heap)
    print(len(heap))