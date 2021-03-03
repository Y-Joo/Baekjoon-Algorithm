import collections, heapq
def course(n, k, times):
    graph = collections.defaultdict(list)
    for a, b, c in times:
        graph[a].append((b,c))
    queue = [(0,k)]
    dist=collections.defaultdict(int)
    while queue:
        time, node= heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt=time+w
                heapq.heappush(queue, (alt, v))
    if len(dist) == n:
        return max(dist.values())
    return -1