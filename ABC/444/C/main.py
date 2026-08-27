import sys
sys.setrecursionlimit(10**6)

from collections import deque
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    As = list(map(int, input_data[1:]))
    #print(As)

    max_a = max(As)
    min_a = min(As)
    #print(max_a, min_a)

    cond = [max_a, max_a + min_a]
    #print(cond)


    ans_list = []
    for c in cond:
        #print(c)
        frag = True
        count_dict = defaultdict(int)
        #print("c=", c)
        for a in As:
            count_dict[a] += 1
        que = []
        for k, v in count_dict.items():
            if k*2 == c and v % 2 == 0:
                continue
            elif k*2 == c:
                frag = False
                break
            que.append((k, v))
        que.sort()
        #print(que)

        if not frag:
            continue

        if not que:
            ans_list.append(c)
            continue
        
        if que[-1][0] == c:
            que.pop(-1)
        #print(que)

        que = deque(que)
        #print(que)
        if len(que) % 2 == 1:
            frag = False
            continue
        else:
            while que:
                r = que.pop()
                l = que.popleft()
                if r[0]+l[0] == c and r[1] == l[1]:
                    continue
                else:
                    frag = False
                    break
        if frag:
            ans_list.append(c)

    print(*ans_list)
    

if __name__ == '__main__':
    main()