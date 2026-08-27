import sys
sys.setrecursionlimit(10**6)

import heapq
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = int(input_data[0])
    K = int(input_data[1])
    
    As = list(map(int, input_data[2:]))

    #sums = []
    #heapq.heapify(sums)
    set_a = set(As)
    sums = defaultdict(int)

    for a in As:
        sums[a] += a
    
    que = [v for v in sums.values()]
    heapq.heapify(que)
    #print(que)
    

    ans = 0
    for i in range(len(set_a)-K):
        ans += heapq.heappop(que)

    print(ans)



if __name__ == '__main__':
    main()