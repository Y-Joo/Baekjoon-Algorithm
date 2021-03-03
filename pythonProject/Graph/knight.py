def bfs():
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    queue = [(cur_x, cur_y, 0)]
    visited = [[0] * (n) for _ in range(n)]
    visited[cur_x][cur_y] = 1
    while queue:
        x, y, cnt = queue.pop(0)
        if x == des_x and y == des_y:
            return cnt
        for i in range(8):
            lx, ly = x + dx[i], y + dy[i]
            if 0 <= lx < n and 0 <= ly < n:
                if visited[lx][ly] == 0:
                    queue.append((lx, ly, cnt + 1))
                    visited[lx][ly] = 1


t = int(input())
for _ in range(t):
    n = int(input())
    cur_x, cur_y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    print(bfs())
