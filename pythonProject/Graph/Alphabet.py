def bfs(start):
    pas = set()
    pas.add(board[0][0])
    queue = set([start])
    m = 1
    while queue:
        x, y, cnt, passed = queue.pop()
        m = max(m, cnt)
        for i in range(4):
            lx, ly = x + dx[i], y + dy[i]
            if 0 <= lx < r and 0 <= ly < c:
                if board[lx][ly] not in passed:
                    queue.add((lx, ly, cnt + 1, passed + board[lx][ly]))
    return m


r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs((0,0,1,board[0][0])))
