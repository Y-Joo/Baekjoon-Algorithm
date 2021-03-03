from typing import List
import sys
sys.setrecursionlimit(100000)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x:int, y:int):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        lx=x+dx[i]
        ly=y+dy[i]
        if 0<=lx<m and 0<=ly<n:
            if mat[lx][ly]<mat[x][y]:
                dp[x][y]+=dfs(lx, ly)
    return dp[x][y]

m, n = map(int, input().split())
mat = [[0 for _ in range(n)] for i in range(m)]
for i in range(m):
    nums = list(map(int, input().split()))
    for j in range(n):
        mat[i][j] = nums[j]
dp=[[-1 for _ in range(n)] for i in range(m)]
print(dfs(0,0))
