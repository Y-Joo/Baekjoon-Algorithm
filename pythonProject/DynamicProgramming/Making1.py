def making_one(n:int):
    d=[0]*(n+1)
    for i in range(2, n+1):
        d[i]=d[i-1]+1
        if i%2==0:
            d[i]=min(d[i//2]+1, d[i])
        if i%3==0:
            d[i]=min(d[i//3]+1, d[i])
    return d[n]

n=int(input())
print(making_one(n))