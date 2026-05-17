"""

num = 12
for i in range(30):
    happy = 0
    while num:
        dig = num % 10
        num //= 10
        #print(dig, num)
        happy += dig**2

    print(happy)
    num = happy

"""

num = int(input())

is_happy = False
for i in range(100):
    happy = 0
    while num:
        dig = num % 10
        num //= 10
        #print(dig, num)
        happy += dig**2

    #print(happy)
    num = happy
    if happy == 1:
        is_happy = True

if is_happy:
    print("Yes")
else:
    print("No")
