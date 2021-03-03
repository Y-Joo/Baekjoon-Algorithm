import collections, heapq
from copy import deepcopy


def Cheapest(n, edges, src,dst, k):
    graph=collections.defaultdict(list)
    for a, b, price in edges:
        graph[a].append((b, price))
    if k==0:
        for d, p in graph[src]:
            if d==dst:
                return p
        return -1
    alt=0
    prices=[]
    queue=[(src,0, k)]
    while queue:
        node, price, cnt= heapq.heappop(queue)
        if node == dst:
            return price
        if k>=0:
            for d, p in graph[node]:
                alt=price + p
                heapq.heappush(queue, (d, alt, k-1))

    return -1

deepcopy