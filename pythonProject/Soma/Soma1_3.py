a, b, c=map(int, input().split())
nums=list(map(int, input().split()))
dis=[]
for num in nums:
    dist=c-num
    if dist<0:
        temp=dist
        dist*=-1
    else:
        temp=dist
    dis.append((dist, temp))
dis.sort()
min_dis=0
for i in range(b):
    if dis[i][1]<0:
        min_dis=min(min_dis, dis[i][1])
print(dis[b-1][0]-min_dis)


