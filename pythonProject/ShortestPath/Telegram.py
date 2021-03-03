from typing import List
import collections, sys, heapq

input = sys.stdin.readline


class Solution:
    def daijkstra(self, n: int, m: int, start: int, graph: List[List[int]])->set:
        INF=1e9
        distance=[INF]*(n+1)
        distance[start]=0
        q=[]
        heapq.heappush(q,(0,start))
        while q:
            dis, now=heapq.heappop(q)
            if distance[now]<dis:
                continue
            for i in graph[now]:
                cost=dis+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))
        cnt=0
        time=0
        for i in range(1,n+1):
            if distance[i]<INF and distance[i]!=0:
                cnt+=1
                time=max(time, distance[i])
        return (cnt,time)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

sol=Solution()
print(*sol.daijkstra(n,m,start,graph))