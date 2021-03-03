import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        lx, ly = x + dx[i], y + dy[i]
        if 0 <= lx < n and 0 <= ly < n:
            if forest[x][y]<forest[lx][ly]:
                dp[x][y] = max(dp[x][y], dfs(lx, ly) + 1)
    return dp[x][y]


forest = []
n = int(input())
for i in range(n):
    forest.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        dfs(i, j)
max_=0
for i in range(n):
    max_=max(max_, max(dp[i]))
print(max_)
