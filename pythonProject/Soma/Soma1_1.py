import collections


def dfs(v, path=[]):
    visited.append(v)
    if v not in graph.keys():
        print(path + [v])
        return
    for w in graph[v]:
        dfs(w, path+[v])


graph = collections.defaultdict(list)
skill=list(input().split())
n = int(input())
for i in range(n):
    a, b = input().split()

    graph[a].append(b)
visited = []
for key in graph.keys():
    if key not in visited:
        dfs(key)