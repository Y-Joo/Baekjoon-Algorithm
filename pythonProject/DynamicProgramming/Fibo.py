from typing import List


class Solution:

    def fibo(self, n: int, d:List[int]) -> int:
        d[1] = 1
        d[2] = 1
        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n]

sol=Solution()
print(sol.fibo(99k,[0]*100))