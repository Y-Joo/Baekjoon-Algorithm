from typing import List
import collections


def DFS(graph: dict, start: int):
    stack = []
    visited = []
    stack.append(start)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for node in graph[v]:
                stack.append(node)
    return len(visited) - 1


n = int(input())
m = int(input())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(DFS(graph, 1))
