import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    T = int(input_data[1])
    
    As = list(map(int, input_data[2:]))

    sum_time = 0
    open_time = 0
    open = True
    for i in range(N):
        if As[i] > open_time:
            open = True
        if open:
            sum_time += As[i] - open_time
            open_time = As[i] + 100
            open = False
    if open_time < T:
        sum_time += T - open_time
    
    print(sum_time)



if __name__ == '__main__':
    main()