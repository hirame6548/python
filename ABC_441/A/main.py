p, q = map(int, input().split())
x, y = map(int, input().split())

if p <= x and x < p+100 and q <= y and y < q+100:
    print("Yes")

else:
    print("No")