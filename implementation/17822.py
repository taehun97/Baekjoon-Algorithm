import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
stencils = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, v):
    q = deque()
    q.append((x, y))
    initial_num = stencils[x][y]
    isAdjacentExists = False
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], (cy + dy[i])%m
            if 0<=nx<n and not v[nx][ny] and stencils[nx][ny]==initial_num:
                if not isAdjacentExists: isAdjacentExists = True
                stencils[nx][ny] = 'x'
                v[nx][ny] = True
                q.append((nx, ny))
                
    if isAdjacentExists: stencils[x][y] = 'x'
    
    return isAdjacentExists

def getStencilsAvg():
    cnt = 0
    sum = 0
    for i in range(n):
        for j in range(m):
            if stencils[i][j]=='x': continue
            else:
                sum += stencils[i][j]
                cnt += 1
    
    return sum/cnt if cnt!=0 else 0

def getStencilsSum():
    result = 0
    for i in range(n):
        for j in range(m):
            if stencils[i][j]=='x': continue
            result += stencils[i][j]
                
    return result    

for _ in range(t):
    # x 배수인 원판을 d 방향으로 k칸 회전
    # d: 0 => 시계방향 | 1 => 반시계방향
    x, d, k = map(int, input().split())
    
    # phase 1
    i = 1
    while x*i-1<len(stencils):
        if d==0: # 시계방향 회전
            stencils[x*i-1] = stencils[x*i-1][-k:] + stencils[x*i-1][:m-k]
        else: # 반시계방향 회전
            stencils[x*i-1] = stencils[x*i-1][k:] + stencils[x*i-1][:k]
        i += 1
            
    # phase 2
    isAdjacent = False
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            local_isAdjacent = False
            
            if stencils[i][j]=='x': continue
            
            if not visited[i][j]:
                visited[i][j] = True
                local_isAdjacent = bfs(i, j, visited)
                if not isAdjacent: isAdjacent = local_isAdjacent
                
    if not isAdjacent:
        avg = getStencilsAvg()
        for i in range(n):
            for j in range(m):
                if stencils[i][j]=='x': continue
                
                if stencils[i][j]>avg:
                    stencils[i][j] -= 1
                elif stencils[i][j]<avg:
                    stencils[i][j] += 1
                    
print(getStencilsSum())