import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

rectangle = [tuple(map(int, input().split())) for _ in range(k)]
grid = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    grid[x][y] = 1
    area = 1
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==-1:
                q.append((nx, ny))
                grid[nx][ny] = 1
                area += 1
    
    return area                

for i in range(k):
    start_y, start_x, end_y, end_x = rectangle[i]
    for j in range(start_x, end_x):
        for k in range(start_y, end_y):
            grid[j][k] = 0



answer = 0
area = []            
for i in range(m):
    for j in range(n):
        if grid[i][j]==-1:
            answer += 1
            area.append(bfs(i, j))

print(answer)
area.sort()
print(*area)