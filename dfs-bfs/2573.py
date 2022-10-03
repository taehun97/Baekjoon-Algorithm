from re import L
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
sea = [list(map(int, input().split())) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt():
    changed_ice = []
    result = 0
    
    for i in range(n):
        for j in range(m):
            if sea[i][j]==0: continue
            melt_size = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0<=nx<n and 0<=ny<m and sea[nx][ny]==0:
                    melt_size += 1
            if sea[i][j]<=melt_size:
                changed_ice.append((i, j, 0))
            else:
                changed_ice.append((i, j, sea[i][j]-melt_size))
            
    for (x, y, size) in changed_ice:
        sea[x][y] = size
        result += size
        
    return result

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()    
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<m and sea[nx][ny]!=0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                
    
    
year = 0
total_bulk = float('inf')
chunk_num = 0

while total_bulk!=0:
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if sea[i][j]!=0 and not visited[i][j]:
                bfs(i, j)
                chunk_num += 1    
    
    if chunk_num>=2:
        print(year)
        exit()
    else: year += 1
    
    total_bulk = melt()
    
    chunk_num = 0
    
print(0)