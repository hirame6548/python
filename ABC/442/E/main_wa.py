import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    Q = int(input_data[1])

    xyab_iter = map(int, input_data[2:])

    arg_l = []
    for i in range(N):
        x = next(xyab_iter)
        y = next(xyab_iter)
        loc = -1
        if y == 0:
            if x > 0:
                loc = 0
            else:
                loc = 4
        elif y < 0:
            if x > 0:
                loc = 1
            elif x == 0:
                loc = 2
            else:
                loc = 3
        else: # y > 0
            if x < 0:
                loc = 5
            elif x == 0:
                loc = 6
            else:
                loc = 7
        arg = 0
        if x != 0 and y != 0:
            arg = -y / x
        #print(loc, arg)
        arg_l.append((loc, arg, i))
    arg_l.sort()
    #print(arg_l)

    idx = [0] * N
    arg_dict = defaultdict(int)
    f_sum = 0
    for n in range(N):
        loc, arg, i = arg_l[n]
        idx[i] = n
        if n != 0:
            if (loc, arg) != (f_loc, f_arg):
                f_sum = arg_dict[(f_loc, f_arg)][1]
        arg_dict[(loc, arg)] = (f_sum, n+1)
        f_loc, f_arg = loc, arg
    #print(idx)
    #print(arg_dict)


    for _ in range(Q):
        a = next(xyab_iter) - 1
        b = next(xyab_iter) - 1
        a_loc, a_arg, a_i = arg_l[idx[a]]
        b_loc, b_arg, b_i = arg_l[idx[b]]
        a_angle = (a_loc, a_arg)
        b_angle = (b_loc, b_arg)
        if a_angle <= b_angle:
            print(arg_dict[b_angle][1] - arg_dict[a_angle][0])

        else: # idx[a] > idx[b]:
            print(N + arg_dict[b_angle][1] - arg_dict[a_angle][0])
    

if __name__ == '__main__':
    main()