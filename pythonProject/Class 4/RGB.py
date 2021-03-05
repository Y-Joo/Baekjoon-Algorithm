import sys
sys.setrecursionlimit(100000)
def rgb(x: int, y: int):
    if x==n-1:
        dp[x][y]=nums[x][y]
        return dp[x][y]
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y]=1e9
    for i in range(3):
        if i == y:
            continue
        dp[x][y] = min(dp[x][y], nums[x][y] + rgb(x + 1, i))
    return dp[x][y]


n = int(input())
dp = [[0] * 3 for _ in range(n)]
nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))
for i in range(3):
    rgb(0,i)
print(min(dp[0]))