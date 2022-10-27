import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dq = deque()

def destroyMineral(b, c, x, y):
    move = 0
    if y==0: move = 1
    elif y==c-1: move = -1
    
    cur_x = x
    cur_y = y
    while 0<=cur_y<c:
        if b[cur_x][cur_y]=='.':
            cur_y += move
        else:
            b[cur_x][cur_y] = '.'
            break
        
    for d in range(4):
        nx, ny = cur_x + dx[d], cur_y + dy[d]
        if 0<=nx<R and 0<=ny<C and b[nx][ny]=='x':
            dq.append((nx, ny))

def bfs(x, y):
    visited = [[False for _ in range(C)] for _ in range(R)]
    fall_list = []
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        
        if cx==R-1: return
        
        if board[cx+1][cy]=='.':
            fall_list.append((cx, cy))
        
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and board[nx][ny]=='x':
                visited[nx][ny] = True
                q.append((nx, ny))
                
    fall(visited, fall_list)
    
def fall(v, f_list):
    k = 1
    flag = False
    while True:
        for x, y in f_list:
            if x+k==R-1:
                flag = True
                break
            
            if board[x+k+1][y]=='x' and not v[x+k+1][y]:
                flag = True
                break
        if flag: break    
        k+=1
        
    for i in range(R-2, -1, -1):
        for j in range(C):
            if v[i][j] and board[i][j]=='x':
                board[i][j] = '.'
                board[i+k][j] = 'x'

N = int(input())
row_list = list(map(int, input().split()))
for i in range(N):   
    visited = [[False for _ in range(C)] for _ in range(R)]
    row = R - row_list[i]
    col = -1
    if i%2==0: col = 0
    else: col = C - 1
    
    destroyMineral(board, C, row, col)
    
    while dq:
        x, y = dq.popleft()
        bfs(x, y)

for i in range(R):
    for j in range(C):
        print(board[i][j], end='')
    print()