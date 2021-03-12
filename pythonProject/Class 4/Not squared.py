from math import ceil
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
r = [0 for i in range(a, b + 1)]
s = [i ** 2 for i in range(2, 1000001)]
n = 2
for i in s:
    if a // i * i < a:
        num = (a // i + 1) * i - a
    else:
        num = ceil(a / i) * i - a
    while num <= b - a:
        r[num] = 1
        num += i
result = 0
for i in r:
    if i == 0: result += 1
print(result)