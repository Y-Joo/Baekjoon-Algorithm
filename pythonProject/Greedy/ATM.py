from typing import List


def atm(n: int, nums: List[int]):
    sum = 0
    presum = 0
    for i in range(n):
        sum += presum + nums[i]
        presum += nums[i]
    return sum


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(atm(n, nums))
