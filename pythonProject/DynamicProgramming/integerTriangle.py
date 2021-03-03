from typing import List


def max_sum(tri: List):
    dp = [[0 for _ in range(i + 1)] for i in range(n)]
    dp[0][0] = tri[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j] + tri[i][j], dp[i - 1][j - 1] + tri[i][j])
    return max(dp[n - 1])


n = int(input())
triangle = []
for i in range(n):
    if i == 0:
        triangle.append([int(input())])
    else:
        nums = list(map(int, input().split()))
        triangle.append(nums)
print(max_sum(triangle))
