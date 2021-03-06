import sys, collections, heapq
input = sys.stdin.readline
INF=int(1e9)

n, m=map(int, input().split())
start=int(input())
graph=collections.defaultdict()
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dis, now=heapq.heappop(q)

        if distance[now]<dis:
            continue
        for i in graph[now]:
            cost=dis+i[1]
            if cost<i[1]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])

