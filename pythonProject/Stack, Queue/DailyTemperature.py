def DailyTemperature(nums:list[int])->list[int]:
    stack=[]
    days=[]*len(nums)
    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            last=stack.pop()
            days[last]=i-last
        stack.append(i)

    return days