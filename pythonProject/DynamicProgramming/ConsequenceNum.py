from typing import List
import sys

sys.setrecursionlimit(100000)


class Solution:
    def consequence(self, n: int, nums: List[int]):
        max_num = -1001
        sum = -1001
        for i in range(0, n):
            if i == 0:
                sum = nums[i]
                max_num=max(max_num, sum)
            else:
                if sum + nums[i] < 0:
                    max_num = max(max_num, nums[i])
                    sum = nums[i]
                else:
                    if sum<0:
                        sum=nums[i]
                        max_num = max(max_num, sum)
                    else:
                        sum += nums[i]
                        max_num=max(max_num, sum)

        return max_num

sol = Solution()
n = int(input())
nums = list(map(int, input().split()))
print(sol.consequence(n, nums))
