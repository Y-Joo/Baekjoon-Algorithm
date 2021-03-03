import sys
sys.setrecursionlimit(100000)
def max_dfs(x, y):
    if max_dp[x][y]!=0:
        return max_dp[x][y]
    if x==n-1:
        return nums[x][y]
    max_dp[x][y]=nums[x][y]
    for i in range(-1, 2):
        ly=y+i
        lx=x+1
        if 0<=ly<3:
            max_dp[x][y]=max(max_dp[x][y], nums[x][y]+max_dfs(lx, ly))
    return max_dp[x][y]

def min_dfs(x, y):
    if min_dp[x][y]!=0:
        return min_dp[x][y]
    if x==n-1:
        return nums[x][y]
    min_dp[x][y]=1000000
    for i in range(-1, 2):
        ly=y+i
        lx=x+1
        if 0<=ly<3:
            min_dp[x][y]=min(min_dp[x][y], nums[x][y]+min_dfs(lx, ly))
    return min_dp[x][y]


n=int(input())
nums=[]
for i in range(n):
    nums.append(list(map(int, input().split())))
max_dp=[[0]*3 for _ in range(n)]
min_dp=[[0]*3 for _ in range(n)]
for i in range(3):
    max_dfs(0,i)
    min_dfs(0,i)
print(max(max_dp[0]), min(min_dp[0]))