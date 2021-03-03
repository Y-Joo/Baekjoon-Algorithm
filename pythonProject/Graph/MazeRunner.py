from typing import List


class Solution:
    def shortest(self, n: int, m: int, grid: List[List[int]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = [(0, 0)]
        visited = [(0, 0)]
        while queue:
            x, y = queue.pop(0)
            print(x,y)
            if x==n-1 and y==m-1:
                return grid[n-1][m-1]
            for i in range(4):
                lx=x+dx[i]
                ly=y+dy[i]
                if lx<0 or lx>=n:
                    continue
                if ly<0 or ly>=m:
                    continue
                if grid[lx][ly]==1 and (lx,ly) not in visited:
                    queue.append((lx,ly))
                    grid[lx][ly]=grid[x][y]+1
                    visited.append((lx,ly))

sol = Solution()
grid = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
print(sol.shortest(5, 6, grid))
