import itertools
def subsets(nums):
    result=[]
    result.append([])
    def dfs(index, path):
        if path not in result:
            result.append(path)

        for i in range(index, len(nums)):
            if [nums[i]] not in path:
                dfs(i+1, path + [nums[i]])

    dfs(0, [])
    return result

nums=input().split()

print(subsets(nums))
