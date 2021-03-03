from typing import List


class Solution:
    def lis(self, n: int, nums: List[int]):
        length = [0] * n
        for k in range(n):
            length[k] = 1
            for i in range(k):
                if nums[i] < nums[k]:
                    length[k] = max(length[k], length[i] + 1)

        INF = 1e9
        cache = [-1] * n

        def find(start: int):
            if cache[start] != -1:
                return cache[start]
            ret = 0
            for i in range(start + 1, n):
                if nums[start] > nums[i]:
                    ret = max(ret, find(i) + 1)
                cache[start] = ret
            return ret

        m = length[0] + find(0)
        for i in range(1, n):
            m = max(m, length[i] + find(i))
        return m


n = int(input())
nums = list(map(int, input().split()))
sol = Solution()
print(sol.lis(n, nums))
