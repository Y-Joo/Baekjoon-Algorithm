from typing import List


class Solution:
    def combine(self, n: int, nums: List[int]):
        min_sum = [0] * (n + 1)
        min_sum[n - 1] = nums[0] + nums[1]
        for i in range(2, n):
            if i == 2:
                min_sum[n - i] = 2 * min_sum[n - i + 1] + nums[i]
            else:
                min_sum[n - i] = min(2 * min_sum[n - i + 1] + nums[i], 2 * (min_sum[n - i + 2] + nums[i] + nums[i - 1]))
            print(nums[i], min_sum[n - i])
        return min_sum[1]


sol = Solution()
t = int(input())
for _ in range(t):
    k = int(input())
    pages = list(map(int, input().split()))
    pages.sort()
    print(sol.combine(k, pages))
