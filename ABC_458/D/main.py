import sys
import heapq

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    X = input_data[0]
    Q = input_data[1]

    ab_iter = iter(input_data[2:])

    s = []
    l = []
    heapq.heapify(s)
    heapq.heapify(l)
    c = X

    for i in range(Q):
        A = next(ab_iter)
        B = next(ab_iter)

        if A > B: # 必ず A <= B
            A, B = B, A

        if c < A:
            heapq.heappush(l, A)
            heapq.heappush(l, B)
            heapq.heappush(s, -c)
            c = heapq.heappop(l)

        elif A <= c < B:
            heapq.heappush(s, -A)
            heapq.heappush(l, B)
        else: # B <= c
            heapq.heappush(s, -A)
            heapq.heappush(s, -B)
            heapq.heappush(l, c)
            c = (-1) * heapq.heappop(s)

        print(c)


if __name__ == '__main__':
    main()