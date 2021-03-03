import collections
from typing import List

p, n, h = map(int, input().split())
sum = [0] * (p+1)
time = [h] * (p+1)
graph = collections.defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
for i in range(p):
    graph[i].sort()
for key in graph.keys():
    for value in graph[key]:
        if value <= time[key]:
            sum[key] += value * 1000
            time[key] -= value
for i in range(1, p + 1):
    print(i, sum[i])
