import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    T = int(input_data[0])
    c_iter = map(int, (input_data[1:]))

    for i in range(T):
        x_1 = next(c_iter)
        y_1 = next(c_iter)
        r_1 = next(c_iter)
        x_2 = next(c_iter)
        y_2 = next(c_iter)
        r_2 = next(c_iter)

        dist = ((x_2 - x_1)**2) + ((y_2 - y_1)**2)

        if (r_1+r_2)**2 >= dist and (r_1-r_2)**2 <= dist:
            print("Yes")
        else:
            print("No")
    
    

if __name__ == '__main__':
    main()