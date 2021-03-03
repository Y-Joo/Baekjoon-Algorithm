n = int(input())
nums = list(map(int, input().split()))
print(nums)
max_count = 0
for i in range(3):
    first = i
    pos = i + nums[i]
    cnt = 2
    while first != pos:
        pos += nums[pos]
        cnt += 1
    max_count = max(max_count, cnt)
print(max_count)
