N, L, R = list(map(int, input().split()))

S = input()

counter = 0
k_dict = {}
k = set()
for i in range(N):
    if L <= i <= R:
        if S[i-L] in k:
            k_dict[S[i-L]] += 1
        else:
            k_dict[S[i-L]] = 1
            k.add(S[i-L])
        #print(k_dict, k)
    elif R < i:
        if S[i-L] in k:
            k_dict[S[i-L]] += 1
        else:
            k_dict[S[i-L]] = 1
            k.add(S[i-L])
        k_dict[S[i-R-1]] -= 1
        if k_dict[S[i-R-1]] == 0:
            k.remove(S[i-R-1])
        #print(k_dict, k)
    if S[i] in k:
        counter += k_dict[S[i]]
    #print(d, counter)
print(counter)


"""

辞書にない key を選んでも、0 を返してくれる

from collections import defaultdict

# デフォルト値 0 を返す辞書を使用
window_counts = defaultdict(int)


"""