N = int(input())

output = ""
for i in range(N, 0, -1):
    output += str(i)
    if i != 1:
        output += ","

print(output)