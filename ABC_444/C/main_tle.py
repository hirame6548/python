import sys
sys.setrecursionlimit(10**6)

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
        As_copy = [i for i in As]
        rest_list = []
        #print("c=", c)
        for a in As_copy:
            #print("a=", a)
            if a == c:
                continue
            elif not a in rest_list:
                rest_list.append(c - a)
            else:
                rest_list.remove(a)
            #print(rest_list)
        if not rest_list:
            ans_list.append(c)

    print(*ans_list)


if __name__ == '__main__':
    main()