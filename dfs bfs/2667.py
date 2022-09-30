import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
h_list = []

def bfs(x, y):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    house_cnt = 1
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny]==1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                house_cnt += 1
                
    return house_cnt

for i in range(N):
    for j in range(N):
        if board[i][j]==1 and not visited[i][j]:
            cnt += 1
            h_list.append(bfs(i, j))
            
h_list.sort()
print(cnt)
for h in h_list:
    print(h)