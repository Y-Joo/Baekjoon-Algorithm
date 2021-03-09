import sys
def check_visited(x, y, count):
    for i in range(count + 1):
        if visited[x][y][i]:
            return True
    return False

def icebreaking(a, b):
    queue = [(a, b, 0)]
    visited[a][b][0] = 1
    mint = r * c
    while queue:
        x, y, count = queue.pop(0)
        for i in range(4):
            lx, ly = x + dx[i], y + dy[i]
            if 0 <= lx < r and 0 <= ly < c:
                if lake[lx][ly] == 'L' and not check_visited(lx, ly, count) and lx != a and ly != b:
                    if count % 2 == 1:
                        count += 1
                    mint = min(mint, count // 2)
                    continue
                if lake[lx][ly] == '.' and not check_visited(lx, ly, count):
                    visited[lx][ly][count] = 1
                    queue.append((lx, ly, count))
                elif lake[lx][ly] == 'X' and not check_visited(lx, ly, count):
                    visited[lx][ly][count] = 1
                    queue.append((lx, ly, count + 1))
    return mint


r, c = map(int, input().split())
lake = []
for i in range(r):
    lake.append(list(map(str, input().strip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * (r + c) for i in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            print(icebreaking(i, j))
            sys.exit()
