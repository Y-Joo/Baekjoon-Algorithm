def bfs(nums, n, m):
    queue = [(0, 0, 1)]
    passed = []
    passed.append((0, 0))
    while queue:
        x, y, dist = queue.pop(0)
        if x == n - 1 and y == m - 1:
            return dist

        else:
            if x > 0 and (x - 1, y) not in passed and nums[x - 1][y] == '1':
                queue.append((x - 1, y, dist + 1))
                passed.append((x - 1, y))
            if x < n - 1 and (x + 1, y) not in passed and nums[x + 1][y] == '1':
                queue.append((x + 1, y, dist + 1))
                passed.append((x + 1, y))
            if y > 0 and (x, y - 1) not in passed and nums[x][y - 1] == '1':
                queue.append((x, y - 1, dist + 1))
                passed.append((x, y - 1))
            if y < m - 1 and (x, y + 1) not in passed and nums[x][y + 1] == '1':
                queue.append((x, y + 1, dist + 1))
                passed.append((x, y + 1))


n, m = map(int, input().split())
nums = [[0 for col in range(m)] for row in range(n)]
for i in range(n):
    nums[i] = input()
print(bfs(nums, n, m))

