from typing import List


class Solution:

    def ant_worrior(self, nums: List[int], n: int, d: List[int]) -> int:
        d[0] = nums[0]
        d[1] = nums[1]
        d[2] = nums[2]+nums[0]
 k
        for i in range(3, n):
            d[i] = max(nums[i] + d[i - 2], nums[i] + d[i - 3])
        return max(d[n - 1], d[n - 2])


sol = Solution()
n = int(input())
nums = list(map(int, input().split()))
print(sol.ant_worrior(nums, n, [0] * 101))
