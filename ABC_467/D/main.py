import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    T = int(input_data[0])
    case_iter = map(int, input_data[1:])

    for i in range(T):
        px = next(case_iter)
        py = next(case_iter)
        qx = next(case_iter)
        qy = next(case_iter)
        rx = next(case_iter)
        ry = next(case_iter)
        sx = next(case_iter)
        sy = next(case_iter)
        dpqx = px-qx
        dpqy = py-qy
        drsx = rx-sx
        drsy = ry-sy

        if dpqx*drsy != dpqy*drsx:
            print("Yes")
        else:
            #print(px, py, qx, qy, rx, ry, sx, sy)
            #print(((px-rx)**2) + ((py-ry)**2), ((qx-sx)**2) + ((qy-sy)**2))
            if ((px-rx)**2) + ((py-ry)**2) == ((qx-sx)**2) + ((qy-sy)**2) and ((px-sx)**2) + ((py-sy)**2) == ((qx-rx)**2) + ((qy-ry)**2):
                print("Yes")
            else:
                print("No")
    

if __name__ == '__main__':
    main()