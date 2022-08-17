import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
level = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def rotate(x, y, l):
    q = deque()
    
    for i in range(x, x+l):
        q.append(grid[i][y:y+l])
        
    for i in range(y, y+l):
        temp = q.pop()
        for j in range(l):
            grid[x+j][i] = temp[j]
            
def sumOfGrid():
    total_sum = 0
    
    for i in range(2**n):
        total_sum += sum(grid[i])
        
    return total_sum

def getMaxChunk():
    visited = [[False for _ in range(2**n)] for _ in range(2**n)]
    result = 0
    
    for i in range(2**n):
        for j in range(2**n):
            if grid[i][j]!=0 and not visited[i][j]:
                local_result = bfs(i, j, visited)
                result = max(local_result, result)
                
    return result
                
def bfs(x, y, v):
    q = deque()
    q.append((x, y))
    v[x][y] = True
    result = 1
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<2**n and 0<=ny<2**n and not v[nx][ny] and grid[nx][ny]!=0:
                result += 1
                v[nx][ny] = True
                q.append((nx, ny))
                
    return result    
        

for l in range(q):
    for i in range(0, 2**n, 2**level[l]):
        for j in range(0, 2**n, 2**level[l]):
            rotate(i, j, 2**level[l])
    
    reduced_ice = []
    for i in range(2**n):
        for j in range(2**n):
            if grid[i][j]==0: continue
            if (i==0 or i==2**n-1) and (j==0 or j==2**n-1):
                reduced_ice.append((i, j))
            elif ((i==0 or i==2**n-1) and (j!=0 and j!=2**n-1)) or ((j==0 or j==2**n-1) and (i!=0 and i!=2**n-1)):
                empty_space = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0<=nx<2**n and 0<=ny<2**n and grid[nx][ny]==0:
                        empty_space += 1
                if empty_space>=1:
                    reduced_ice.append((i, j))
            else:
                empty_space = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0<=nx<2**n and 0<=ny<2**n and grid[nx][ny]==0:
                        empty_space += 1
                if empty_space>=2:
                    reduced_ice.append((i, j))
                    
    for rx, ry in reduced_ice:
        grid[rx][ry] -= 1
        
print(sumOfGrid())   
print(getMaxChunk())