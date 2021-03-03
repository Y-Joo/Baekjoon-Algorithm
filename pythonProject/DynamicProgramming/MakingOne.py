from typing import List


class Solution:

    def making_one(self, n: int, d: List[int]) -> int:
        for i in range(2, n + 1):
            d[i] = d[i - 1] + 1
            if i % 2 == 0:
                d[i] = min(d[i // 2] + 1, d[i])
            if i % 3 == 0:
                d[i] = min(d[i // 3] + 1, d[i])
            if i % 5 == 0:
                d[i] = min(d[i // 5] + 1, d[i])
        return d[n]


sol = Solution()
n = int(input())
print(sol.making_one(n, [0] * 30001))
