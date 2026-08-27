import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    H = int(input_data[0])
    W = int(input_data[1])
    
    Ss = input_data[2:]

    counter = 0

    # 積集合について判定し、あとで同じマスを選出する場合を一回分足して2で割る
    for h_1 in range(H):
        for w_1 in range(W):
            for h_2 in range(h_1, H):
                for w_2 in range(w_1, W):
                    if judge(Ss, h_1, w_1, h_2, w_2):
                        counter += 1

    print(counter)






def judge(matrix, h_1, w_1, h_2, w_2):
    H = h_2 - h_1 + 1
    W = w_2 - w_1 + 1
    for h in range(H):
        for w in range(W):
            if matrix[h_1+h][w_1+w] == matrix[h_2-h][w_2-w]:
                continue
            else:
                return False
    return True






if __name__ == '__main__':
    main()