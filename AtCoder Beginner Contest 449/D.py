L, R, D, U = list(map(int, input().split()))


x_l = list(range(L, R+1, 2))
diff = 0

if L % 2 == 0:
    l_x = L
else:
    l_x = L+1
if R % 2 == 0:
    r_x = R
else:
    r_x = R-1

dot = len(range(l_x, r_x+1, 2)) * len(range(D, U+1))

for y in range(D, U+1):
    if y % 2 == 0:
        if L % 2 == 0:
            y_l = max(L+1, -abs(y)+1)
        else:
            y_l = max(L, -abs(y)+1)
        if R % 2 == 0:
            y_r = min(R-1, abs(y)-1)
        else:
            y_r = min(R, abs(y)-1)
        diff += len(range(y_l, y_r+1, 2))
        #print("y=",y, "diff=",diff)
    else:
        if L % 2 == 0:
            y_l = max(L, -abs(y)+1)
        else:
            y_l = max(L+1, -abs(y)+1)
        if R % 2 == 0:
            y_r = min(R, abs(y)-1)
        else:
            y_r = min(R-1, abs(y)-1)
        diff -= len(range(y_l, y_r+1, 2))
        #print("y=",y, "diff=",diff)


print(dot + diff)