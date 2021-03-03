import collections
def reconstruct(locations):
    graph = collections.defaultdict(list)
    for a, b in sorted(locations):
        graph[a].append(b)

    route=[]

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    return route[::-1]

locations=[]
strs=[str for str in input().split(',')]

for str in strs:
    t=str.split(' ')
    locations.append(t)
print(reconstruct((locations)))
