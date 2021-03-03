def dfs():
    for i in range(n + 1):
        dp[i][1] = 1

    for j in range(n + 1):
        for r in range(j + 1):
            for i in range(2, k + 1):
                dp[j][i] += dp[r][i - 1]
                dp[j][i] %= 1000000000
    return dp[n][k]


n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
print(dfs())
