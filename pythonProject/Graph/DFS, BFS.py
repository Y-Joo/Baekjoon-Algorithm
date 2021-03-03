from typing import List
import collections

def DFS(graph:dict, start:int):
    stack=[]
    visited=[]
    stack.append(start)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for node in graph[v]:
                stack.append(node)
    return visited

def BFS(graph:dict, start:int):
    queue = []
    visited = []
    queue.append(start)
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            for node in graph[v]:
                queue.append(node)
    return visited

n, m, v=map(int, input().split())
graph=collections.defaultdict(list)
for _ in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for key in graph.keys():
    graph[key].sort(reverse=1)
print(*DFS(graph, v))
for key in graph.keys():
    graph[key].sort()
print(*BFS(graph,v))