from typing import List


class Solution:
    def lis(self, n: int, nums: List):
        length = [0] * n
        for k in range(n):
            length[k] = 1
            for i in range(k):
                if nums[i][1] < nums[k][1]:
                    length[k] = max(length[k], length[i] + 1)
        m = length[0]
        for i in range(1, n):
            m = max(m, length[i])
        return n - m


n = int(input())
nums = [(0, 0)] * n
for i in range(n):
    a, b = map(int, input().split())
    nums[i] = (a, b)
nums.sort()
sol = Solution()
print(sol.lis(n, nums))
