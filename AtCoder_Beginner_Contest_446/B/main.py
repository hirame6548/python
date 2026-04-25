import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = int(input_data[0])
    M = int(input_data[1])
    
    LXs = iter(input_data[2:])

    xs = []
    for _ in range(N):
        L = next(LXs)
        add_list = []
        for x in range(L):
            add_list.append(next(LXs))
        xs.append(add_list)
    #print(xs)


    no_drink = set()
    for i in range(N):
        frag = True
        for drink in xs[i]:
            if not drink in no_drink:
                no_drink.add(drink)
                frag = False
                print(drink)
                break
        if frag:
            print("0")



    

if __name__ == '__main__':
    main()