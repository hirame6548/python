import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    s = input_data[0]
    
    s_set = set(s)

    s_list = list(s_set)
    s_count = [0 for _ in range(len(s_list))]

    for i in range(len(s_list)):
        s_count[i] = s.count(s_list[i])

    max_c = max(s_count)

    del_list = []
    for i in range(len(s_list)):
        if s_count[i] == max_c:
            del_list.append(s_list[i])

    ans = ""
    for ans_s in s:
        if not ans_s in del_list:
            ans += ans_s
    
    print(ans)


    

if __name__ == '__main__':
    main()