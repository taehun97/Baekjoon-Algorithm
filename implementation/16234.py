import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global isBorderOpened
    
    q = deque()
    acumulated_q = []
    q.append((x, y))
    acumulated_q.append((x, y))
    visited[x][y] = True
    
    sum = board[x][y]
    
    while q:
        cx, cy = q.popleft()
    
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[nx][ny]-board[cx][cy])<=r:
                isBorderOpened = True
                visited[nx][ny] = True
                sum += board[nx][ny]
                q.append((nx, ny))
                acumulated_q.append((nx, ny))
    
    if len(acumulated_q):      
        for (ax, ay) in acumulated_q:
            board[ax][ay] = sum//len(acumulated_q)
        

turn = 0
while True:
    # 격자 모양으로 탐색
    candidate = deque([(i,j) for i in range(n) for j in range(i%2, n, 2)])
    visited = [[False]*n for _ in range(n)]
    isBorderOpened = False
    for _ in range(len(candidate)):
        i, j = candidate.popleft()
        if not visited[i][j]:
            bfs(i, j)
    
    if not isBorderOpened: break
    else: turn += 1
    
print(turn)