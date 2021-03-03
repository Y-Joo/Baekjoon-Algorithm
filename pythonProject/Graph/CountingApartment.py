from typing import List
import sys


def DFS(n: int, graph: List, x: int, y: int):
    stack = []
    visited = []
    stack.append((x, y))
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    while stack:
        i, j = stack.pop()
        graph[i][j] = 0
        for k in range(4):
            lx = i + dx[k]
            ly = j + dy[k]
            if 0 <= lx < n and 0 <= ly < n and (lx, ly) not in visited and graph[lx][ly] == '1':
                stack.append((lx, ly))
                visited.append((lx, ly))
    return len(visited)+1


n = int(input())
graph = [[0 for _ in range(n+1)]for i in range(n)]
cnt = []
c=0
for i in range(n):
    str=sys.stdin.readline()
    for j, char in enumerate(str):
        graph[i][j]=char
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            cnt.append(DFS(n, graph, i, j))
            c+=1
print(c)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])
