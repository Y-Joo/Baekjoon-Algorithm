import collections
nums=collections.deque()
n=int(input())
for i in range(1, n+1):
    nums.append(i)
while len(nums)>1:
    nums.popleft()
    b=nums.popleft()
    nums.append(b)
print(nums[0])