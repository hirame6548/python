import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    Ss = input_data[1:]
    
    max_len = 0
    for i in range(N):
        max_len = max(max_len, len(Ss[i]))

    for i in range(N):
        dot = (max_len - len(Ss[i])) // 2
        print("."*dot + Ss[i] + "."*dot)

    

if __name__ == '__main__':
    main()