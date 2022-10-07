import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input())
board = []

max_height = 0
max_district_cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    for j in range(N):
        max_height = max(max_height, row[j])

def bfs(x, y, h, v):
    v[x][y] = True
    queue = deque()
    queue.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not v[nx][ny] and board[nx][ny]>h:
                v[nx][ny] = True
                queue.append((nx, ny))

for height in range(max_height+1):
    visited = [[False]*N for _ in range(N)]
    local_district_cnt= 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j]>height:
                bfs(i, j, height, visited)
                local_district_cnt += 1
                
    max_district_cnt = max(max_district_cnt, local_district_cnt)
    
print(max_district_cnt)