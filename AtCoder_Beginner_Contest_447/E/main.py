import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

# a = [int(x) for x in input_data[2:]]  3番目（インデックス2）以降のすべてをリスト a として受け取る例
# even = a[0::2]  index が偶数のものだけ取り出す例
    N = int(input_data[0])
    M = int(input_data[1])
    
    iter_data = iter(list(map(int, input_data[2:])))

    us = []
    vs = []
    for _ in range(M):
        us.append(next(iter_data)-1)
        vs.append(next(iter_data)-1)

    #print(N, M, us, vs)


    uf = list(range(N))
    #print(uf)
    uf = UnionFind(N)

    frag = True
    for i in range(M-1, -1, -1):
        uf.union(us[i], vs[i])
        print(i, us[i], vs[i])
        if uf.pare_num == 1 and frag:
            per_uni = i
            frag = False

    # クエリを逆順に、つまり M から順に下っていくと、 per_uni 番目にすべての点がつながる
    # その一つ手前から、per_uni 番目を飛ばして枝数 2 を維持できるような辺をまた考えれば良い
    # 再帰のほうがいいかも
    print(per_uni)



class UnionFind:
# 宣言は list = UnionFind(), 以下の self はこの list を指す, list は基本 list(range(N))
# list.parent: つながっている木の代表値を返す, list.size: つながっている木の長さを返す
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.pare_num = n

    # list.find(x): xが属する木の代表値を返す
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # list.union(x, y): x が属する木と, y が属する木を結合
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.pare_num -= 1
        return True

    # list.same(x, y): x が属する木と y が属する木が同じか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)



if __name__ == '__main__':
    main()