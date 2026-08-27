import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    S = input_data[0]
    T = input_data[1]
    
    r_S = S.replace("A", "")
    r_T = T.replace("A", "")

    if r_S != r_T:
        print(-1)
    
    else:
        s_list = A_count(S)
        t_list = A_count(T)

        ans = 0
        for i in range(len(s_list)):
            ans += s_list[i] + t_list[i] - (min(s_list[i], t_list[i]) * 2)

        print(ans)



def A_count(S):
    counter = 0
    ans = []
    for s in S:
        if s == "A":
            counter += 1
        else:
            ans.append(counter)
            counter = 0
    ans.append(counter)
    return ans


if __name__ == '__main__':
    main()