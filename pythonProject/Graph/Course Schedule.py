import collections
def course(n, courses):
    graph = collections.defaultdict(list)
    for a, b in courses:
        graph[a].append(b)
    passed=[]

    def dfs(a):
        if graph[a] in passed:
            return False
        passed.append(a)
        for i in graph[a]:
            if not dfs(i):
                return False
        passed.remove(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True