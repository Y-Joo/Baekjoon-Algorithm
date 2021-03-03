n = int(input())

nums = list(map(int, input().split()))
max_cnt = 0
for i in range(3):
    first = i
    pos = i + nums[i]
    cnt = 2
    while first != pos:
        pos += nums[pos]
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)