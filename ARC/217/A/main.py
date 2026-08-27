import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return

    T = input_data[0]
    cases = input_data[1:]


    for c in cases:
        ans = []
        c += 1

        cycle = c // 4
        rest = c % 4

        for i in range(cycle):
            ans.append(4*i)
            ans.append(4*i+1)
            ans.append(4*i+3)
            ans.append(4*i+2)
        
        for i in range(rest):
            ans.append(i+4*cycle)

        print(*ans[1:])    
    

if __name__ == '__main__':
    main()