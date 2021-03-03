from typing import List
def wine(n:int, nums:List[int]):
    d=[0]*n
    if n==0:
        return 0
    d[0]=nums[0]
    if n==1:
        return d[0]
    d[1]=nums[0]+nums[1]
    if n==2:
        return d[1]
    d[2]=max(d[1], d[0]+nums[2], nums[1]+nums[2])
    for i in range(3, n):
        d[i]=max(d[i-1], d[i-2] + nums[i], d[i-3] + nums[i-1]+nums[i])
    return d[n-1]

n=int(input())
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
print(wine(n,nums))