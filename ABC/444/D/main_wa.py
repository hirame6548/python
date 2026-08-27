import sys
sys.setrecursionlimit(10**6)

from collections import deque


def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    As = list(map(int, input_data[1:]))
    #print(As)

    As.sort()

    As_sub = []

    As_sub.append(As[0])
    for i in range(len(As)-1):
        As_sub.append(As[i+1] - As[i])
    #print(As_sub)

    dig_num = len(As_sub)
    #print(dig_num)

    ans_list = deque([])

    frag = False
    for i in range(dig_num):
        digit =  ((dig_num)-i)%10
        # 特殊処理
        if digit == 0:
            ans_list.appendleft(str(digit) * As_sub[i])
            frag = True
        elif frag == True and not As_sub[i] == 0:
            if digit != 9:
                ans_list.appendleft(str(digit) * (As_sub[i]-1) + str(digit+1))
                frag = False
            else:
                ans_list.appendleft(str(0) * As_sub[i])
        else:
            ans_list.appendleft(str(digit) * As_sub[i])
    if frag:
        ans_list.appendleft("1")
        frag = False
    print("".join(ans_list))

    

if __name__ == '__main__':
    main()