def combinations(n, k):
    def dfs(index, path):
        if len(path) == k:
            result.append(path)
            return

        for i in range(index, n + 1):
            if i not in path:
                tmp=path.copy()
                tmp.append(i)
                dfs(i + 1, tmp)


    result=[]
    dfs(1, [])
    return result

n=int(input())
k=int(input())
print(combinations(n,k))
