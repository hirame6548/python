import sys
sys.setrecursionlimit(10**6)
import itertools  # case = list(itertools.islice(case_iter, N))
from collections import defaultdict
import math


import math

class Arg:
    __slots__ = ['x', 'y', 'reg', 'id']
    
    def __init__(self, x, y, id=-1):
        self.id = id
        
        if x == 0 and y == 0:
            self.reg = -1
            self.x = 0
            self.y = 0
            return
            
        if x >= 0 and y > 0:
            self.reg = 0
        elif x > 0 and y <= 0:
            self.reg = 1
        elif x <= 0 and y < 0:
            self.reg = 2
        else:
            self.reg = 3
            
        g = math.gcd(abs(x), abs(y))
        self.x = x // g
        self.y = y // g

    def __lt__(self, other):
        if self.reg != other.reg:
            return self.reg < other.reg
        return self.x * other.y - self.y * other.x < 0

    def __eq__(self, other):
        return self.reg == other.reg and self.x * other.y == self.y * other.x

'''
points = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 1)]
args = [Arg(x, y, i) for i, (x, y) in enumerate(points)]
angles.sort() # クラスの __lt__ に従って自動的に誤差なくソートされる

cf. __lt__ と __eq__ しか定義してないから <= とか > は論理演算子で対応
'''



def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    N = int(input_data[0])
    Q = int(input_data[1])

    xyab_iter = map(int, input_data[2:])

    args = []
    for i in range(N):
        x = next(xyab_iter)
        y = next(xyab_iter)
        arg = Arg(x, y, i)
        args.append(arg)
    args.sort()
    
    #for i in range(N):
    #    print(args[i].x, args[i].y, args[i].id)


    idx = [0] * N
    arg_dict = defaultdict(int)
    f_sum = 0
    for n in range(N):
        arg = args[n]
        idx[arg.id] = n
        key = (arg.reg, arg.x, arg.y)
        if n != 0:
            if not key == f_key:
                f_sum = arg_dict[f_key][1]
        arg_dict[key] = (f_sum, n+1)
        f_key = key
    #print(arg_dict)


    for _ in range(Q):
        a = next(xyab_iter) - 1
        b = next(xyab_iter) - 1
        a_arg = args[idx[a]]
        b_arg = args[idx[b]]
        a_key = (a_arg.reg, a_arg.x, a_arg.y)
        b_key = (b_arg.reg, b_arg.x, b_arg.y)

        if a_arg < b_arg or a_arg == b_arg:
            print(arg_dict[b_key][1] - arg_dict[a_key][0])

        else: # idx[a] > idx[b]:
            print(N + arg_dict[b_key][1] - arg_dict[a_key][0])


if __name__ == '__main__':
    main()
