import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    S = input_data[0]

    c = [0, 0, 0]
    for s in S:
        if s == "A":
            c[0] += 1
        elif s == "B":
            if c[0] > c[1]:
                c[1] += 1
        else:
            if c[1] > c[2]:
                c[2] += 1

    print(c[2])
 

if __name__ == '__main__':
    main()