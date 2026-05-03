N = input()

n_0 = N[0]
frag = True
for n in N:
    #print(n)
    if n != n_0:
        print("No")
        frag = False
        break

if frag:
    print("Yes")