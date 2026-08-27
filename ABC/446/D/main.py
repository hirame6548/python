import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = input_data[0]
    As = input_data[1:]

    src_set = set()
    al_src = set()
    src_dict = {}

    for i in range(N):
        a = As[i]
        #print("start: a", a, "src_set", src_set, "al_src", al_src, "src_dict", src_dict)
        if not a in al_src:
            src_set.add(a+1)
            src_dict[a] = a
            #   print("A")
        if a in src_set:
            src_set.remove(a)
            #print(src_set)
            src_set.add(a+1)
            src_dict[a] = src_dict[a-1]
        al_src.add(a)

    
    c_max = 0
    for k in src_dict:
        c_max = max(c_max, k - src_dict[k] + 1)

    print(c_max)



if __name__ == '__main__':
    main()