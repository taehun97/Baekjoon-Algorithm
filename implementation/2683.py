import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isCheezeAllMelted():
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1: return False
                        
    return True

def checkOutside():
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and not isOutside[nx][ny]:
                q.append((nx, ny))
                isOutside[nx][ny] = True

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        cx, cy = q.popleft()
        if exposedDimension(cx, cy)>=2: grid[cx][cy] = 0

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<m and not isChecked[nx][ny] and grid[nx][ny]==1:
                q.append((nx, ny))
                isChecked[nx][ny] = True
                

def exposedDimension(x, y):
    result = 0
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and isOutside[nx][ny]:
            result += 1
            
    return result

time = 0
while not isCheezeAllMelted():
    time += 1
    isOutside = [[False for _ in range(m)] for _ in range(n)]
    isChecked = [[False for _ in range(m)] for _ in range(n)]
    
    checkOutside()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not isChecked[i][j]:
                bfs(i, j)
                
print(time)
                    
    