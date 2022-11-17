import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
        
def bfs(x, y):
    check[x][y] = True
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<=2000 and 0<=ny<=2000 and not check[nx][ny] and board[nx][ny]==1:
                check[nx][ny] = True
                queue.append((nx, ny))
                
board = [[0 for _ in range(2001)] for _ in range(2001)]                
check = [[False for _ in range(2001)] for _ in range(2001)]

ans = 0
rec_list = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = (x1 + 500) * 2, (y1 + 500) * 2
    x2, y2 = (x2 + 500) * 2, (y2 + 500) * 2

    rec_list.append((x1, y1))

    for i in range(x1, x2+1):
        if i==x1 or i==x2:
            for j in range(y1, y2+1):
                board[i][j] = 1
        else:
            board[i][y1] = 1
            board[i][y2] = 1
    
for x, y in rec_list:
    if not check[x][y]:
        bfs(x, y)
        ans += 1

if check[1000][1000]: ans -= 1        
print(ans)