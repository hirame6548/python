import sys
sys.setrecursionlimit(10**6)
#import itertools  # case = list(itertools.islice(case_iter, N))
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    M = int(input_data[1])
    
    A = list(map(int, input_data[2:N+2]))
    B = list(map(int, input_data[N+2:]))
    #print(A, B)

    heapq.heapify(A)
    heapq.heapify(B)

    counter = 0
    while A and B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        if a*2 >= b:
            counter += 1
            continue
        elif A:
            while A:
                a = heapq.heappop(A)
                if a*2 >= b:
                    counter += 1
                    break


    print(counter)

if __name__ == '__main__':
    main()