import sys


def self_dfs(graph, i, j) :

    if i<0 or i>=len(graph) or \
        j<0 or j>=len(graph[0]) or \
        graph[i][j] != '1':
        return

    graph[i][j]= 0
    self_dfs(graph, i - 1, j)
    self_dfs(graph, i + 1, j)
    self_dfs(graph, i, j - 1)
    self_dfs(graph, i, j + 1)


graph = [[0 for col in range(6)] for row in range(4)]
for i in range(4):
    str=sys.stdin.readline()
    for j, char in enumerate(str):
        graph[i][j]=char
cnt=0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]=='1':
            self_dfs(graph, i, j)
            cnt+=1
print(cnt)