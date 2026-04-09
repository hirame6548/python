import sys

search_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 入力：matrix = 行列
# 出力：周囲をすべて0で囲んだ行列
# メリット：隣接 4 マスサーチに例外処理がいらなくなる、行数、列数と index が一致する
def add_border(matrix):
    # row_num = 行数, col_num = 列数
    row_num = len(matrix)
    col_num = len(matrix[0])
    matrix.insert(0, [0]*col_num)
    matrix.append([0]*col_num)
    for i in range(row_num+2):
        matrix[i].insert(0, 0)
        matrix[i].append(0)
    return matrix

# 入力：数値の二重リスト
# 出力：二重リスト内の数値の最大値
def max_in_list(list_list):
    max_list = []
    for i in range(len(list_list)):
        max_list.append(max(list_list[i]))
    return max(max_list)

# 入力：number = 探したい値, matrix = 探知対象の行列
# 出力：値の座標(タプル)のリスト
def search_matrix(number, matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                result.append((i, j))
    return result

# 入力：cord = 座標(タプル), matrix = 対象の行列
# 出力：隣接 4 マスが入力座標の値 -1 と一致する場合 = True, else = False, 
#      入力座標の値が 0 の場合 = false
def next_src(cord, matrix):
    edited_cord_value = matrix[cord[0]][cord[1]] - 1
    # 値が 0 ならFalse
    if edited_cord_value == 0:
        return False
    # 隣接4マスをサーチ
    else:
        for di, dj in search_direction:
            if matrix[cord[0]+di][cord[1]+dj] == edited_cord_value:
                return True
        return False

# 入力：cord = 座標, matrix = 行列
# 出力：隣接 4 マスのうち、入力座標の値 -1 と一致するならその座標のリスト、そうでないなら None
def next_cord(cord, matrix):
    edited_cord_value = matrix[cord[0]][cord[1]] - 1
    next_cord_list = []
    if edited_cord_value == 0:
        return None
    else:
        for di, dj in search_direction:
            if matrix[cord[0]+di][cord[1]+dj] == edited_cord_value:
                next_cord_list.append((cord[0]+di, cord[1]+dj))
        if len(next_cord_list) > 0:
            return next_cord_list
        else:
            return None

# 入力：cord = 座標, matrix = 行列, path = 移動経路(タプルのリスト)
# 出力：一歩先の移動経路(タプルのリスト)のリスト
def next_path_list(cord, matrix, path):
    paths = []
    # next_cord(cord, matrix) にはタプルのリストが入ってる
    next_cord_list = next_cord(cord, matrix)
    for i in range(len(next_cord_list)):
        path_copy = path.copy()
        path_copy.append(next_cord_list[i])
        paths.append(path_copy)
    return paths

# 入力：path_list = 移動経路(タプルのリスト)のリスト, matrix = 行列
# 出力：いずれかの入力経路の現在位置から移動可能であればTrue, そうでなければFalse
def path_src(path_list, matrix):
    for i in range(len(path_list)):
        if next_src(path_list[i][-1], matrix):
            return True
    return False

# 入力：cord = 座標, matrix = 行列
# 出力：移動経路(タプルのリスト)のリスト
def path_list(cord, matrix):
    path_list = [[cord]]
    if not next_src(cord, matrix):
        return path_list
    else:
        # 移動可能な経路がある限り、経路を更新する
        while path_src(path_list, matrix):
            for i in range(len(path_list)):
                if next_src(path_list[i][-1], matrix):
                    path_list.extend(next_path_list(path_list[i][-1], matrix, path_list[i]))
                    path_list.remove(path_list[i])
        return path_list

# 入力：matrix = 行列
# 出力：最大値をとる座標から始まる、最長移動経路（タプルのリスト）
def max_path(matrix):
    cord_list = []
    max_value = max_in_list(matrix)
    cord_list = search_matrix(max_value, matrix)
    paths = []
    for i in range(len(cord_list)):
        paths.extend(path_list(cord_list[i], matrix))
    max_path = paths[max(range(len(paths)), key=lambda x: len(paths[x]))]
    return max_path

# 入力：matrix = 行列
# 出力：最大移動経路の値を 1 ずつ減らした行列
def matrix_reduce(matrix):
    path = []
    path = max_path(matrix)
    for i in range(len(path)):
        matrix[path[i][0]][path[i][1]] -= 1
    return matrix

# 入力：matrix = 行列
# 出力：移動経路(タプルのリスト)
def output_path(matrix):
    path = []
    while max_in_list(matrix) > 0:
        path.extend(max_path(matrix))
        matrix = matrix_reduce(matrix)
    return path




# 行数が不明な場合も対応できるよう、rangeを指定せず for 文を用いて読み込み
grid = []
for line in sys.stdin:
    row = list(map(int, line.split()))
    grid.append(row)

# 行列のサイズ
size = len(grid)

# 行列の外側に 0 を挿入
grid = add_border(grid)

# 経路の取得（タプルのリスト）
path = output_path(grid)

# 成型して出力
for i in range(len(path)):
    print(f"{path[i][0]} {path[i][1]}")
