from typing import List


class Solution:
    def floyd_warshall(self, n: int, m: int, distance: List[List[int]]):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    distance[i][j] = 0

        for k in range(1, n + 1):
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])


n, m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print("INFINITY")
        else:
            print(distance[i][j])
