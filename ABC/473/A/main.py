N = int(input())
A = list(map(int, input().split()))

half = N // 2

print(sum(A[half:]))