n, m = map(int, input().split())
if m > n:
    n, m = m, n
for i in range(m, 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)
        break
for i in range(n, 10001):
    if i % n == 0 and i % m == 0:
        print(i)
        break
