from typing import List

def coin(n:int, k:int, coins:List[int]):
    d=[0]*(k+1)
    d[0]=1
    for coin in coins:
        for i in range(1, k+1):
            if i-coin>=0:
                d[i]+=d[i-coin]
    return d[k]

n, k=map(int, input().split())
coins=[0]*n
for i in range(n):
    coins[i]=int(input())
print(coin(n, k, coins))
