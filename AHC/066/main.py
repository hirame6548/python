import sys
from collections import deque

def solve():
    # 入力の高速読み込み
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])

    idx = 3
    # 縦方向の壁（左右のマスを区切る壁）
    v_walls = []
    for _ in range(N):
        v_walls.append(input_data[idx])
        idx += 1

    # 横方向の壁（上下のマスを区切る壁）
    h_walls = []
    for _ in range(N - 1):
        h_walls.append(input_data[idx])
        idx += 1

    balls = []
    baskets = []
    for _ in range(M):
        br, bc = int(input_data[idx]), int(input_data[idx+1])
        dr, dc = int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        balls.append((br, bc))
        baskets.append((dr, dc))

    # グラフの構築 (隣接リスト)
    # adj[r][c] = [(next_r, next_c, direction_code)]
    # direction_code: 0:右(Right), 1:下(Down), 2:左(Left), 3:上(Up)
    adj = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 右への移動 (壁が '0' なら移動可能)
            if j + 1 < N and v_walls[i][j] == '0':
                adj[i][j].append((i, j + 1, 0))
                adj[i][j + 1].append((i, j, 2))
            # 下への移動 (壁が '0' なら移動可能)
            if i + 1 < N and h_walls[i][j] == '0':
                adj[i][j].append((i + 1, j, 1))
                adj[i + 1][j].append((i, j, 3))

    def navigate(path, current_dir):
        """方向の配列(path)から、F, R, Lの操作列を生成する"""
        cmds = []
        cd = current_dir
        for d in path:
            diff = (d - cd) % 4
            if diff == 1:
                cmds.append('R')
            elif diff == 2:
                # 後ろを向く場合は右に2回(または左に2回)
                cmds.append('R')
                cmds.append('R')
            elif diff == 3:
                cmds.append('L')
            cmds.append('F')
            cd = d
        return cmds, cd

    def get_path(sr, sc, gr, gc):
        """2点間の最短経路(方向の配列)をBFSで求める"""
        q = deque([(sr, sc)])
        parent = {(sr, sc): None}
        while q:
            r, c = q.popleft()
            if r == gr and c == gc:
                break
            for nr, nc, d in adj[r][c]:
                if (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c, d)
                    q.append((nr, nc))
        
        path = []
        curr = (gr, gc)
        while curr != (sr, sc):
            pr, pc, d = parent[curr]
            path.append(d)
            curr = (pr, pc)
        path.reverse()
        return path

    ans = []
    curr_r, curr_c = 0, 0
    curr_dir = 0  # 初期状態は右(0)を向いている

    unpicked = set(range(M))

    # すべてのボールを回収・配達するまでループ
    while unpicked:
        # 1. 現在地から最も近い未回収のボールをBFSで探す
        q = deque([(curr_r, curr_c)])
        parent = {(curr_r, curr_c): None}
        target_k = -1
        
        ball_pos_to_id = {balls[k]: k for k in unpicked}
        
        while q:
            r, c = q.popleft()
            if (r, c) in ball_pos_to_id:
                target_k = ball_pos_to_id[(r, c)]
                break
            for nr, nc, d in adj[r][c]:
                if (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c, d)
                    q.append((nr, nc))
                    
        # 最も近いボールまでの経路を復元
        path = []
        curr = balls[target_k]
        while curr != (curr_r, curr_c):
            pr, pc, d = parent[curr]
            path.append(d)
            curr = (pr, pc)
        path.reverse()
        
        # ボールへ移動して拾う
        cmds, curr_dir = navigate(path, curr_dir)
        ans.extend(cmds)
        ans.append('S')
        curr_r, curr_c = balls[target_k]
        
        # 2. 拾ったボールを対応するカゴへ運ぶ
        gr, gc = baskets[target_k]
        path_to_basket = get_path(curr_r, curr_c, gr, gc)
        
        cmds, curr_dir = navigate(path_to_basket, curr_dir)
        ans.extend(cmds)
        ans.append('S')
        curr_r, curr_c = gr, gc
        
        # 回収完了としてセットから削除
        unpicked.remove(target_k)
        
        # T回を超えてしまう場合は、問題の制約上途中でも打ち切る処理を入れるか検討する
        # （ベースラインなので今回は最後まで積む）

    # 1行ずつ出力
    print("\n".join(ans))

if __name__ == '__main__':
    solve()