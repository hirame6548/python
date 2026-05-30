A, B = map(int, input().split())

l = ["1", "2", "3"]
if A == B:
    print(-1)
else:
    l.remove(A)
    l.remove(B)
    print(l[0])
