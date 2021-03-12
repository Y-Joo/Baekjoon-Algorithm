n = int(input())
nums = list(map(int, input().split()))
nums.sort()
i, j = 0, len(nums) - 1
mingap = 2000000000
mini = 0
minj = 0
while i < j:
    sum = nums[i] + nums[j]
    gap = abs(sum)
    if gap<mingap:
        mingap = gap
        mini, minj = nums[i], nums[j]
    if sum < 0:
        i += 1
    elif sum > 0:
        j -= 1
    else:
        break
print(mini, minj)