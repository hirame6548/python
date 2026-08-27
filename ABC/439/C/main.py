# ハックできないか？　あらかじめ満たす整数をリストにしといて、それから出力すればいいじゃん

#print(3200**2)

N = int(input())

max_n = int(N ** (1/2))
#print(max_n)

pro_list = []
for i in range(1, max_n+1):
    pro_list.append(i**2)

#print(pro_list)

ans_set = set()
ans_del = set()
for i in range(max_n):
    if not i == max_n + 1:
        for j in range(i+1, max_n):
            ans = pro_list[i] + pro_list[j]
            if ans > N:
                break
            if ans in ans_set:
                ans_del.add(ans)
            ans_set.add(ans)

ans_list = list(ans_set - ans_del)
ans_list.sort()

print(len(ans_list))
print(*ans_list)