N = int(input()) #5

A_list = [] #[5, 5, 4, 5, 3]
B_list = [] #[3, 2, 1, 1, 2]


for i in range(N):
    A_i, B_i = map(int, input().split())
    A_list.append(A_i)
    B_list.append(B_i)

M = int(input()) #8

S_list = [] #['retro', 'chris', 'itchy', 'tuna', 'crab', 'rock', 'cod', 'ash']
for _ in range(M):
    S_list.append(input())


judge_list = ["No"] * M

"""
list = [ [{}] [{} {}] [{} {} {}] ]
list[i] = 文字列の長さがiのもののリスト
list[i][j] = 文字列の長さがiのものの、j文字目の集合
"""

#dig_set_list = [[set() for i in range(1, N+1)] for _ in range(i)] #[[{}], [{}, {}], [{}, {}, {}], [{}, {}, {}, {}], [{}, {}, {}, {}, {}]]
"""
dig_set_list = []
for i in range(1, N+1):
    dig_set_list.append([])
    for j in range(i):
        dig_set_list[i-1].append(set())
"""

# [[set()], [set(), set()], [set(), set(), set()], [set(), set(), set(), set()], [set(), set(), set(), set(), set()]]
dig_set_list = [[set() for _ in range(i)] for i in range(1, 10 + 1)] 
#print(dig_set_list)

# [[set()], [set(), set()], [{'c', 'a'}, {'s', 'o'}, {'d', 'h'}], [{'r', 'c', 't'}, {'r', 'u', 'o'}, {'n', 'c', 'a'}, {'b', 'k', 'a'}], [{'r', 'c', 'i'}, {'h', 't', 'e'}, {'r', 'c', 't'}, {'r', 'i', 'h'}, {'y', 's', 'o'}]]
for i in range(M):
    l = len(S_list[i])
    for j in range(l):
        #print(i, j, l)
        dig_set_list[l-1][j].add(S_list[i][j])



judge = None
for i in range(M):
    #print(S_list[i])
    if len(S_list[i]) == N:
        #print(i)
        for j in range(N):
            #print(i, j, A_list[j])
            #print(S_list[i][j])
            #print(dig_set_list[A_list[j]-1][B_list[j]-1])
            if not S_list[i][j] in dig_set_list[A_list[j]-1][B_list[j]-1]:
                judge = False
                break
            judge = True
    else:
        judge = False

    if judge:
        print("Yes")
    else:
        print("No")