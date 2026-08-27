def main():
    N, K = map(int, input().split())
    #print(N, K)

    lines = []
    for i in range(N):
        lines.append(list(map(int, input().split())))

    C = map(int, input().split())


    for i in range(N):
        c_c = next(C)
        LS = c_c * lines[i][0]
        idx = i
        if LS >= K:
            break
        K -= LS
    
    c_k = (K-1) % lines[idx][0]
    #print(c_k)

    print(lines[idx][c_k+1])
    

if __name__ == '__main__':
    main()