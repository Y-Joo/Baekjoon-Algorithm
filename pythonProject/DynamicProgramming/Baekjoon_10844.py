from typing import List


class Solution:
    def stair_number(self, n):
        d = [0] * n
        nums = [[0] * 10 for _ in range(n)]
        for i in range(n):
            for j in range(10):
                if i == 0:
                    if j == 0:
                        continue
                    d[i] += 1
                    nums[i][j] += 1
                else:
                    if i == 1 and j == 1:
                        d[i] += 1
                        nums[i][j] += 1
                    elif j == 0:
                        d[i] += nums[i - 1][1]
                        nums[i][0] += nums[i - 1][1]
                    elif j == 9:
                        d[i] += nums[i - 1][8]
                        nums[i][9] += nums[i - 1][8]
                    else:
                        d[i] = d[i] + nums[i - 1][j - 1] + nums[i - 1][j + 1]
                        nums[i][j] += nums[i - 1][j - 1] + nums[i - 1][j + 1]

        return d[n - 1] % 1000000000


n = int(input())
sol = Solution()
print(sol.stair_number(n))
