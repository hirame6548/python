import sys
sys.setrecursionlimit(10**6)

from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    H = int(input_data[0])
    W = int(input_data[1])
    N = int(input_data[2])

    hws = iter(list(map(int, input_data[3:])))

    hs = []
    ws = []
    hw = []
    for i in range(N):
        h = next(hws)
        w = next(hws)
        hs.append((h, i))
        ws.append((w, i))
        hw.append((h, w))
    hs.sort()
    ws.sort()

    hs = deque(hs)
    ws = deque(ws)

    #print(hs, ws)  # [(1, 1), (1, 3), (2, 0), (3, 2), (3, 4), (4, 5)] [(1, 2), (1, 4), (2, 0), (2, 3), (2, 5), (4, 1)]

    if hs[-1][0] == H:
        drc = 1
    else: # W
        drc = -1

    ans_list = [None for _ in range(N)]

    cur_h = H
    cur_w = W
    while hs and ws:
        if drc == 1: # H
            while hs[-1][0] == cur_h or ans_list[hs[-1][1]]:
                if ans_list[hs[-1][1]]:
                    hs.pop()
                    if not hs:
                        break
                    continue
                h_v, idx = hs.pop()
                w_v = hw[idx][1]
                ans_list[idx] = (1, cur_w - w_v + 1)
                cur_w -= w_v
                #print("hs, ws, ans_list",hs, ws, ans_list)                
                if not hs:
                    break
        else: # W
            while ws[-1][0] == cur_w or ans_list[ws[-1][1]]:
                if ans_list[ws[-1][1]]:
                    ws.pop()
                    if not ws:
                        break
                    continue
                w_v, idx = ws.pop()
                h_v = hw[idx][0]
                ans_list[idx] = (cur_h - h_v + 1, 1)
                cur_h -= h_v
                #print("hs, ws, ans_list",hs, ws, ans_list)
                if not ws:
                    break
        drc *= -1
        #print("cur_h=",cur_h, "cur_w=",cur_w, "\n")
        #print("___________________________")

    for i in range(N):
        print(*ans_list[i])
    
    

if __name__ == '__main__':
    main()