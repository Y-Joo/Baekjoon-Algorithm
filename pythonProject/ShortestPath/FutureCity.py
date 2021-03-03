from typing import List


class Solution:
    def floyd(self, n: int, m: int, graph: List[List[int]]):

        for k in range(1, n + 1):
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())
for i in range(1, n + 1):
    graph[i][i] = 0
sol = Solution()
sol.floyd(n, m, graph)
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
