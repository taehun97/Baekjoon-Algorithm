import sys
from collections import deque

input = sys.stdin.readline
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(12):
    row = list(input().rstrip("\n"))
    board.insert(0, row)
    
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    coord_list = []
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<12 and 0<=ny<6:
                if visited[nx][ny]==-1:
                    if board[nx][ny]==board[cx][cy]:
                        coord_list.append((nx, ny))
                        visited[nx][ny] = 0
                        q.append((nx, ny))

    return coord_list
                
def roundProcess():
    visited = [[-1 for _ in range(6)] for _ in range(12)]
    isEverExplode = False
    
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.' and visited[i][j]==-1:
                c_list = bfs(i, j, visited)
                if not isEverExplode and len(c_list)>=4:
                    isEverExplode = True
                    
                if len(c_list)<4:
                    for x, y in c_list:
                        visited[x][y] = 1
    
    if not isEverExplode: return False
                
    for i in range(12):
        for j in range(6):
            if visited[i][j]==0: 
                board[i][j] = '.'
        
    fillEmptySpace()
    
    return True
    
def fillEmptySpace():
    for j in range(6):
        temp = []
        for i in range(12):
            if board[i][j]!='.':
                temp.append(board[i][j])
        
        k = 0
        while k<len(temp):
            board[k][j] = temp[k]
            k += 1
            
        for s in range(k, 12):
            if board[s][j]!='.': board[s][j] = '.'
            
            
turn = 0
while roundProcess():    
    turn += 1
    
print(turn)