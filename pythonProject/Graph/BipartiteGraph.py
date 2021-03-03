import collections


def check_bipartite(v: int, e: int, graph: dict):
    visited = [0] * (v + 1)
    flg = [0] * (v + 1)
    for i in range(1, v + 1):
        if visited[i] == 0:
            queue = [i]

            flg[i] = 1
            while queue:
                node = queue.pop(0)
                if visited[node] == 1:
                    continue
                else:
                    visited[node] = 1
                    for t in graph[node]:
                        if flg[t] == 0:
                            queue.append(t)
                            if flg[node] == 1:
                                flg[t] = -1
                            else:
                                flg[t] = 1
                        else:
                            if flg[node] == flg[t]:
                                return False

    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = collections.defaultdict(list)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if check_bipartite(v, e, graph):
        print("YES")
    else:
        print("NO")
