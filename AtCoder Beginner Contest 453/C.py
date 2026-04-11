N = int(input())

from collections import deque
Ls = list(map(int, input().split()))

i_list = [] # ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']
for i in range(2**N):
    i_list.append(bin(i)[2:].zfill(N))

x = 0.5
i_que = deque(i_list)


max_move = 0

for i in range(len(i_list)):
    Ls_que = deque(Ls)
    dir_list = deque(i_que.pop())
    counter = 0
    x = 0.5
    #print(Ls_que, dir_list)
    for j in range(N):
        dir = dir_list.pop()
        #print("A", i, j)
        frag = "None"
        #print(dir)
        if dir == '1':
            if x < 0:
                frag = "minus"
            dx = Ls_que.popleft()
            #print("R, dx=", dx)
            x += dx
            if x > 0 and frag == "minus":
                counter += 1
                #print("count")
        else:
            if x > 0:
                frag = "plus"
            dx = Ls_que.popleft()
            #print("L, dx=", dx)
            x -= dx
            if x < 0 and frag == "plus":
                counter += 1
                #print("count")
            #print(counter)
        #print(x, counter)
    if max_move < counter:
        max_move = counter
        #print("______________")


print(max_move)