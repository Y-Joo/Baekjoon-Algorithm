from typing import List


def stair(n: int, nums: List[int]):
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = nums[0]
    if n == 1:
        return dp[0]
    dp[1] = nums[0] + nums[1]
    if n == 2:
        return dp[1]
    dp[2] = max(nums[1]+nums[2], dp[0] + nums[2])
    if n == 3:
        return dp[2]

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])
    return dp[n - 1]


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
print(stair(n, nums))
