from typing import List


class Solution:
    def coin(self, n: int, k: int, coins: List[int]):
        cnt = 0
        for i in range(n - 1, -1, -1):
            if k <= 0:
                break
            if k >= coins[i]:
                cnt += k // coins[i]
                k %= coins[i]

        return cnt


n, k = map(int, input().split())
coins = [0] * n
sol = Solution()
for i in range(n):
    coins[i] = int(input())
print(sol.coin(n, k, coins))
