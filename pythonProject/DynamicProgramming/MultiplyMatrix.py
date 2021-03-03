from typing import List
import collections

class Solution:
    def multiply_matrix(self, n: int, mat: dict):
        min_multi = float('inf')
        for a, b in mat:



n = int(input())
mats = collections.defaultdict
sol = Solution()
for i in range(n):
    a, b = map(int, input().split())
    mats[a]=b
print(sol.multiply_matrix(n, mats))
