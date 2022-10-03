import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
riped_tomato_coords = []
board = [[] for _ in range(H)]

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))
        board[i].append(row)
        
        for k in range(len(row)):
            if row[k]==1: riped_tomato_coords.append((i, j, k))
        
def bfs():
    queue = deque()
    for x, y, z in riped_tomato_coords:
        queue.append((x, y, z, 0))
        visited[x][y][z] = True
        
    cx, cy, cz, cd = 0, 0, 0, 0
    
    while queue:
        cx, cy, cz, cd = queue.popleft()
        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and board[nx][ny][nz]==0 and not visited[nx][ny][nz]:
                queue.append((nx, ny, nz, cd+1))
                visited[nx][ny][nz] = True
                board[nx][ny][nz] = 1
    
    return cd

def isAllRiped():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if board[i][j][k]==0: return False
    return True

answer = bfs()

if isAllRiped():
    print(answer)
else: print(-1)

