import itertools
def combinations(nums, target):
    result=[]
    def dfs(sum, index, path):
        if sum==target:
            result.append(path)
            return

        for i in range(index, len(nums)):
            if sum + nums[i] <= target:
                dfs(sum + nums[i], i, path + [nums[i]])
        else:
            return

    dfs(0,0,[])
    return result

nums=list(map(int,input().split()))
target=int(input())
print(combinations(nums, target))