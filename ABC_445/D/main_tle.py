import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    H = int(input_data[0])
    W = int(input_data[1])
    N = int(input_data[2])

    hws = iter(list(map(int, input_data[3:])))

    hs = []
    ws = []
    for i in range(N):
        hs.append((next(hws), i))
        ws.append((next(hws), i))
    hs.sort()
    ws.sort()
    #print(hs, ws)

    h_vs = []
    h_ks = []
    w_vs = []
    w_ks = []

    for i in range(N):
        h_v, h_k = hs[i]
        w_v, w_k = ws[i]
        h_vs.append(h_v)
        h_ks.append(h_k)
        w_vs.append(w_v)
        w_ks.append(w_k)
    #print(h_vs, h_ks, w_vs, w_ks) -> [1, 1, 2, 3, 3, 4] [1, 3, 0, 2, 4, 5] [1, 1, 2, 2, 2, 4] [2, 4, 0, 3, 5, 1]


    ans_list = [(-1, -1) for _ in range(N)]

    cur_h = H
    cur_w = W

    while h_vs:
        if h_vs[-1] == cur_h:
            while h_vs and h_vs[-1] == cur_h:
                h_i = len(h_vs) - 1
                h_v = h_vs.pop(h_i)
                h_k = h_ks.pop(h_i)
                w_i = w_ks.index(h_k)
                w_k = w_ks.pop(w_i)
                w_v = w_vs.pop(w_i)
                ans_list[h_k] = (1, cur_w - w_v + 1)
                cur_w -= w_v
        else: # w_vs[-1] == cur_w:
            while h_vs and w_vs[-1] == cur_w:
                w_i = len(w_vs) - 1
                w_v = w_vs.pop(w_i)
                w_k = w_ks.pop(w_i)
                h_i = h_ks.index(w_k)
                h_k = h_ks.pop(h_i)
                h_v = h_vs.pop(h_i)
                ans_list[h_k] = (cur_h - h_v + 1, 1)
                cur_h -= h_v

    for i in range(N):
        print(*ans_list[i])
    
    

if __name__ == '__main__':
    main()