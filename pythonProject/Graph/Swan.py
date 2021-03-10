import sys
def icebreaking(a, b, flag):
    queue=[(a,b)]
    if queue_2 and flag:
        queue=queue_2.copy()
        queue_2.clear()
    visited[a][b]=1
    cnt=0
    while queue:
        x, y=queue.pop(0)
        if lake[x][y]=='L':
            cnt+=1
        if cnt==2:
            return True
        for i in range(4):
            lx,ly=x+dx[i], y+dy[i]
            if 0<=lx<r and 0<=ly<c:
                if (lake[lx][ly]=='.' or lake[lx][ly]=='L') and visited[lx][ly]==0:
                    visited[lx][ly]=1
                    queue.append((lx,ly))
                elif lake[lx][ly]=='X' and visited[lx][ly]==0:
                    visited[lx][ly]=1
                    lake[lx][ly]='.'
                    queue_2.append((lx,ly))
    return False
def check_meeting(a,b):
    queue=[(a,b)]
    if swan_2:
        queue=swan_2.copy()
        swan_2.clear()
    visit[a][b] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            lx, ly = x + dx[i], y + dy[i]
            if 0 <= lx < r and 0 <= ly < c:
                if lake[lx][ly] == '.' and visit[lx][ly] == 0:
                    visit[lx][ly] = 1
                    queue.append((lx, ly))
                elif lake[lx][ly] == 'L' and visit[lx][ly] == 0:
                    return True
                elif lake[lx][ly]=='X' and visit[lx][ly]==0:
                    swan_2.append((lx,ly))
    return False

r, c=map(int, input().split())
lake=[]
for i in range(r):
    lake.append(list(map(str, input().strip())))
queue_2=[]
swan_2=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
days=0
visited=[[0]*c for _ in range(r)]
visit = [[0] * c for _ in range(r)]
swan_x=0
swan_y=0
while 1:
    if not queue_2:
        for i in range(r):
            for j in range(c):
                if (lake[i][j]=='.' or lake[i][j]=='L') and visited[i][j]==0:
                    if icebreaking(i, j, 0):
                        print(days)
                        sys.exit()
                if lake[i][j]=='L':
                    swan_x=i
                    swan_y=j
        days += 1
    else:
        icebreaking(0,0,1)
        days += 1
        if check_meeting(swan_x, swan_y):
            print(days)
            sys.exit()