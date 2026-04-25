# BFS : 幅優先探索、保存しとく情報は多いから比較的メモリは食うが、必ず最短経路が見つかる

from collections import deque

def bfs(N, G, start):
    """
    N: 頂点数
    G: 隣接リスト G[u] = [v1, v2, ...]
    start: 始点
    返り値: 始点からの最短距離のリスト (到達不可は -1)
    """
    dist = [-1] * N
    queue = deque([start])
    dist[start] = 0

    while queue:
        v = queue.popleft()
        for nxt in G[v]:
            if dist[nxt] == -1:  # 未訪問の場合
                dist[nxt] = dist[v] + 1
                queue.append(nxt)
                
    return dist





# DFS : 深さ優先探索、到達可能性の判定、全探索が必須なもの (BFS は最短さえわかれば良い)

from collections import deque

def dfs(N, G, start):
    """
    N: 頂点数
    G: 隣接リスト G[u] = [v1, v2, ...]
    start: 始点
    返り値: 訪問済みかどうかの真偽値リスト
    """
    visited = [False] * N
    stack = [start]
    visited[start] = True

    while stack:
        v = stack.pop()
        for nxt in G[v]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                
    return visited

