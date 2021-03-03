from typing import List
import sys

input = sys.stdin.readline


class Solution:
    def classroom(self, n: int, times: List):
        cnt = 0
        a=0
        for time in times:
            if time[1] >= a:
                cnt += 1
                a=time[0]
        return cnt


n = int(input())
times = []
for i in range(n):
    a, b = map(int, input().split())
    times.append((b, a))
times.sort()
sol = Solution()
print(sol.classroom(n, times))
