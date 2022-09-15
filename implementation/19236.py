import sys
import copy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[] for _ in range(4)]
max_score = 0

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        board[i].append([row[2*j], row[2*j+1]-1])
                
# board[shark_location[0]][shark_location[1]][0] = 's'
def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # fish movement
    for n in range(1, 17):
        f_x, f_y = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0]==n:
                    f_x, f_y = i, j
                    break
                
        if f_x==-1 and f_y==-1: continue
        
        f_d = board[f_x][f_y][1]
        
        for f in range(8):
            nd = (f_d + f) % 8
            nx, ny = f_x + dx[nd], f_y + dy[nd]

            if 0<=nx<4 and 0<=ny<4 and (sx!=nx or sy!=ny):
                board[f_x][f_y][1] = nd
                board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
                break
    
    # shark movement and eatting
    dn = board[sx][sy][1]
    for i in range(1, 5):
        nx, ny = sx + dx[dn] * i, sy + dy[dn] * i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0]>0:
            dfs(nx, ny, score, copy.deepcopy(board))
            
dfs(0, 0, 0, board)
print(max_score)
