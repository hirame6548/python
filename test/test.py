N = int(input())
A = list(map(int, input().split()))

if len(A) == 1:
    print("Yes")

else:
    frag = True
    for i in range(N-1):
        if A[i] * A[1] != A[0] * A[i+1]:
            frag = False

    if frag:
        print("Yes")
    else:
        print("No")
