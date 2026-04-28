import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    S = input_data[1]


    ab = []
    bc = []
    ca = []
    ab_dif = 0
    bc_dif = 0
    ca_dif = 0

    for i in range(N):
        if S[i] == "A":
            ab_dif += 1
            ca_dif -= 1
        elif S[i] == "B":
            bc_dif += 1
            ab_dif -= 1
        else:
            ca_dif += 1
            bc_dif -= 1
        ab.append(ab_dif)
        bc.append(bc_dif)
        ca.append(ca_dif)

    abc = defaultdict(int)
    abc[(0, 0)] = 1
    ab_dict = defaultdict(int)
    bc_dict = defaultdict(int)
    ca_dict = defaultdict(int)
    ab_dict[0] = 1
    bc_dict[0] = 1
    ca_dict[0] = 1
    for i in range(N):
        abc[(ab[i], bc[i])] += 1
        ab_dict[ab[i]] += 1
        bc_dict[bc[i]] += 1
        ca_dict[ca[i]] += 1
    
    abc_sum = 0
    ab_sum = 0
    bc_sum = 0
    ca_sum = 0
    for v in abc.values():
        abc_sum += int(v*(v-1)/2)
    for v in ab_dict.values():
        ab_sum += int(v*(v-1)/2)
    for v in bc_dict.values():
        bc_sum += int(v*(v-1)/2)
    for v in ca_dict.values():
        ca_sum += int(v*(v-1)/2)

    print(int(N*(N+1)/2) - ab_sum - bc_sum - ca_sum + abc_sum*2)


if __name__ == '__main__':
    main()