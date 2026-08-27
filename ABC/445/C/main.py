import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    As = list(map(lambda x :int(x)-1, input_data[1:]))
    #print(As)
    
    visited = set()
    ans_list = [0 for _ in range(N)]

    for i in range(N):
        if not i in visited:
            cur = i
            visited.add(cur)
            cur_visited = set([cur])
            if cur == As[cur]:
                ans_list[cur] = cur+1
            elif As[cur] in visited:
                ans_list[cur] = ans_list[As[cur]]
            while not As[cur] in visited:
                cur = As[cur]
                visited.add(cur)
                cur_visited.add(cur)
                if cur == As[cur]:
                    ans_list[cur] = cur+1
                if As[cur] in visited:
                    ans_list[cur] = ans_list[As[cur]]
            
            for j in cur_visited:
                ans_list[j] = ans_list[cur]
            #print(i, cur, cur_visited, visited, ans_list)
        
    print(" ".join(list(map(str, ans_list))))
    


if __name__ == '__main__':
    main()