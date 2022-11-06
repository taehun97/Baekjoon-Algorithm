import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

start_x, start_y, end_x, end_y = -1, -1, -1, -1

for i in range(N):
    for j in range(N):
        if board[i][j]=='#':
            if start_x==-1 and start_y==-1: start_x, start_y = i, j
            else: end_x, end_y = i, j
            
def bfs(sx, sy, ex, ey, n):
    check = [[[-1 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    
    queue = deque()
    
    for i in range(4):
        check[sx][sy][i] = 0
        queue.append((sx, sy, i))
        
    while queue:
        cx, cy, dir = queue.popleft()
        
        if cx==ex and cy==ey:
            print(check[cx][cy][dir])
            return
        
        nx, ny = cx + dx[dir], cy + dy[dir]
        
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny]!='*':
                if check[nx][ny][dir]==-1 or check[nx][ny][dir]>check[cx][cy][dir]:
                    check[nx][ny][dir] = check[cx][cy][dir]
                    queue.appendleft((nx, ny, dir))
                
                if board[nx][ny]=='!':
                    if dir<2:
                        for i in range(2, 4):
                            if check[nx][ny][i]==-1 or check[nx][ny][i]>check[cx][cy][dir] + 1:
                                check[nx][ny][i] = check[cx][cy][dir] + 1
                                queue.append((nx, ny, i))
                                
                    else:
                        for i in range(2):
                            if check[nx][ny][i]==-1 or check[nx][ny][i]>check[cx][cy][dir] + 1:
                                check[nx][ny][i] = check[cx][cy][dir] + 1
                                queue.append((nx, ny, i))

            
bfs(start_x, start_y, end_x, end_y, N)