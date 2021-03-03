def recursive_dfs(digits):
    def dfs(path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in digits:
            if i not in path:
                dfs(path+i)

    if not digits:
        return []

    result=[]
    dfs("")
    return result

digits=input()
print(recursive_dfs(digits))