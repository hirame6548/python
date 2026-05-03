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
    A_max = As[-1]
    max_dig = A_max + 5

    dig_num = [0 for _ in range(max_dig)]

    for a in As:
        dig_num[a-1] += 1
    #print(dig_num) # [0, 0, 4, 0, 0, 0, 0, 0]

    cnt = [0 for _ in range(max_dig)]
    dig_sum = 0
    for i in range(len(dig_num)-1, -1, -1):
        dig_sum += dig_num[i]
        cnt[i] = dig_sum
    #print(cnt)

    ans = []
    carry = 0
    for i in range(len(cnt)):
        ans.append(str((cnt[i] + carry) % 10))
        carry = (cnt[i] + carry) // 10
        #print(ans[i], carry)

    #print(ans)
    while ans[-1] == "0":
        ans.pop(-1)
    #print(ans)
    
    ans.reverse()

    print("".join(ans))



if __name__ == '__main__':
    main()