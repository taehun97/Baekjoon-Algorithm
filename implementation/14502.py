import sys
import copy
from collections import deque

input = sys.stdin.readline
blueprint = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
safe_area = 0

r, c = map(int, input().split())

def make_wall(cnt):
    if cnt==3:
        bfs()
        return
    
    else:
        for i in range(r):
            for j in range(c):
                if blueprint[i][j]==0:
                    blueprint[i][j] = 1
                    make_wall(cnt + 1)
                    blueprint[i][j] = 0 

def bfs():
    copied_blueprint = copy.deepcopy(blueprint)
    queue = deque()
    
    for i in range(r):
        for j in range(c):
            if copied_blueprint[i][j]==2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<r and 0<=ny<c and copied_blueprint[nx][ny]==0:
                copied_blueprint[nx][ny] = 2
                queue.append((nx, ny))
                
    global safe_area
    local_safe_area = 0
    
    for i in range(r):
        for j in range(c):
            if copied_blueprint[i][j]==0:
                local_safe_area += 1
                
    safe_area = max(safe_area, local_safe_area)
    
    

for _ in range(r):
    row = list(map(int, input().split()))
    blueprint.append(row)
    
make_wall(0)
                                        
print(safe_area)