from typing import List


class Solution:

    def tile(self, n: int, d: List[int]) -> int:
        d[0] = 0
        d[1] = 1
        for i in range(2, n + 1):
            d[i] = (d[i - 1] + d[i - 2] * 2) % 796796
        return d[n]


sol = Solution()
n = int(input())
print(sol.tile(n, [0] * (n + 1)))
