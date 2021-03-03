from typing import List

class Solution:
    def lis(self, n:int, nums:List[int]):
        length=[0]*n
        for k in range(n):
            length[k]=1
            for i in range(k):
                if nums[i]<nums[k]:
                    length[k]=max(length[k],length[i]+1)
        m=length[0]
        for i in range(1,n):
            m=max(m, length[i])
        return m
n=int(input())
nums=list(map(int,input().split()))
sol=Solution()
print(sol.lis(n, nums))

