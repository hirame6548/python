Q = int(input())


vol = 0
stream = -1
for i in range(Q):
    a = int(input())
    if a == 1:
        vol += 1
    elif a == 2:
        if vol > 0:
            vol -= 1
    else:
        stream *= -1

    if stream == 1 and vol >= 3:
        print("Yes")
    else:
        print("No")