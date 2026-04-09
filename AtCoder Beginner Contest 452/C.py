N = int(input()) #5

A_list = [] #[0, 5, 5, 4, 5, 3]
B_list = [] #[3, 2, 1, 1, 2]
A_list.append(0)


for i in range(N):
    A_i, B_i = map(int, input().split())
    A_list.append(A_i)
    B_list.append(B_i)

M = int(input()) #8

S_list = [] #['retro', 'chris', 'itchy', 'tuna', 'crab', 'rock', 'cod', 'ash']
for _ in range(M):
    S_list.append(input())


judge_list = ["No"] * M


for i in range(M):
    if len(S_list[i]) == N: #S_list[i]:脊椎文字列
        for k in range(N): #脊椎の上から順に試行
            for j in range(M): #S_list[j]:肋骨文字列
                B_k = B_list[k]
                dig_judge = False
                if B_k > len(S_list[j]):
                    print("A")
                    dig_judge = False
                elif S_list[j][B_k-1] == S_list[i][k]:
                    dig_judge = True
                    print("B")
                    break
                #print(dig_judge)
            if dig_judge == False:
                judge_list[i] = "No"
                print("C")
                break
        else:
            print("D")
            judge_list[i] = "Yes"
    else:
        print("E")
        judge_list[i] = "No"

    print(judge_list[i])