n=int(input())
nums=list(map(int, input().split()))
x=int(input())
i, j=0, len(nums)-1
cnt=0
nums.sort()
while i<j:
    sum=nums[i]+nums[j]
    if sum==x:
        cnt+=1
        i+=1
        j-=1
    elif sum>x:
        j-=1
    else:
        i+=1
print(cnt)