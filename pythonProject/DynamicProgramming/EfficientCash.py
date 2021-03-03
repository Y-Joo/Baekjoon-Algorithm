from typing import List


class Solution:
    def efficient_cash(self, n: int, m:int, cashes:List[int], d: List[int]) -> int:
        cashes.sort()
        for i in range(cashes[0], m + 1):
            flag=0
            for cash in cashes:
                if i-cash==0:
                    d[i]+=1
                if d[i-cash]!=0:
                    if flag==0:
                        d[i]=d[i-cash] + 1
                        flag=1
                    else:
                        d[i]=min(d[i],d[i - cash] + 1)
        if d[m]==0:
            return -1
        else:
            return d[m]



sol = Solution()
n, m = map(int, input().split())
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
print(sol.efficient_cash(n, m, nums, [0] * (m + 1)))
