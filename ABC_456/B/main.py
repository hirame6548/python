import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    a_1 = input_data[0:6]
    a_2 = input_data[6:12]
    a_3 = input_data[12:18]
    #print(a_1, a_2, a_3)

    perm = [(4, 5, 6), (4, 6, 5), (5, 4, 6), (5, 6, 4), (6, 4, 5), (6, 5, 4)]

    counter = 0
    for i, j, k in perm:
        a1 = a_1.count(i)
        a2 = a_2.count(j)
        a3 = a_3.count(k)
        counter += a1 * a2 * a3

    print(counter / (6**3))
        
    
    

if __name__ == '__main__':
    main()