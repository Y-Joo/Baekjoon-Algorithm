from typing import List


class Solution:
    def num_of_icecreams(self, n: int, m: int, grid: List[List[str]]) -> int:
        cnt = 0

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == '0':
                grid[i][j] = '1'
            else:
                return
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    dfs(i, j)
                    cnt += 1
        return cnt


sol = Solution()
grid = [
    ["0", "0", "1", "1", "0"],
    ["0", "0", "0", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "0", "1", "1"]
]
print(sol.num_of_icecreams(4, 5, grid))
