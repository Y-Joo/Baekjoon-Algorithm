from typing import List
import sys


def BFS(n: int, m: int, graph: List):
    queue = [(0, 0, 1, 1)]
    visited = [[[0 for j in range(2)] for _ in range(m + 1)] for i in range(n)]
    visited[0][0][1]=1
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    while queue:
        i, j, cnt, chance = queue.pop(0)
        if i == n - 1 and j == m - 1:
            return cnt
        for k in range(4):
            lx = i + dx[k]
            ly = j + dy[k]
            if lx < 0 or lx >= n or ly < 0 or ly >= m:
                continue
            if graph[lx][ly] == '0' and visited[lx][ly][chance]!=1:
                queue.append((lx, ly, cnt + 1, chance))
                visited[lx][ly][chance]=1
            elif graph[lx][ly] == '1' and chance == 1:
                queue.append((lx, ly, cnt + 1, chance - 1))
    return -1


n, m = map(int, input().split())
graph = [[0 for _ in range(m + 1)] for i in range(n)]
for i in range(n):
    str = sys.stdin.readline()
    for j, char in enumerate(str):
        graph[i][j] = char
print(BFS(n, m, graph))
