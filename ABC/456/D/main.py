import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    S = input_data[0]


    nabc_cnt = [1, 0, 0, 0] # 確認した最後の文字が None, a, b, c である場合をカウント
    abc_dict = {"a":1, "b":2, "c":3}

    for i in range(len(S)):
        cur_let = abc_dict[S[i]]
        plus = sum(nabc_cnt) - nabc_cnt[cur_let]
        nabc_cnt[cur_let] = (nabc_cnt[cur_let] + plus) % 998244353

    print((sum(nabc_cnt)-1) % 998244353)
    


if __name__ == '__main__':
    main()