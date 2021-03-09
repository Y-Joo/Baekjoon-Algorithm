n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
minpr = price[0]
mini = 0
sum = 0
dist = 0
for i in range(n):
    if i == n - 1:
        sum += minpr * dist
        break
    if minpr > price[i]:
        sum += minpr * dist
        minpr = price[i]
        mini = i
        dist = 0
    dist += dis[i]
print(sum)
