import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
rx, ry = 0, 0
bx, by = 0, 0
exit_x, exit_y = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = []

for i in range(n):
    row = list(input())
    board.append(row)
    for j in range(m):
        if row[j]=='B': bx, by = i, j
        elif row[j]=='R': rx, ry = i, j
        elif row[j]=='O': exit_x, exit_y = i, j
        
visited[rx][ry][bx][by] = True
queue.append((rx, ry, bx, by, 1))
        
def bfs():
    while queue:
        cur_rx, cur_ry, cur_bx, cur_by, cnt = queue.pop(0)
        if cnt>10: break
        
        for i in range(4):
            x1, y1, cnt1 = move(cur_rx, cur_ry, i)
            x2, y2, cnt2 = move(cur_bx, cur_by, i)
            
            if board[x2][y2]!='O':
                if board[x1][y1]=='O':
                    print(cnt)
                    return
                if x1==x2 and y1==y2:
                    if cnt1>cnt2:
                        x1 -= dx[i]
                        y1 -= dy[i]
                    else:
                        x2 -= dx[i]
                        y2 -= dy[i]
                if not visited[x1][y1][x2][y2]:
                    visited[x1][y1][x2][y2] = True
                    queue.append((x1, y1, x2, y2, cnt + 1))
                    
    print(-1)
            
def move(x, y, d):
    cnt = 0
    while board[x + dx[d]][y + dy[d]]!='#' and board[x][y]!='O':
        x += dx[d]
        y += dy[d]
        cnt += 1
            
    return x, y, cnt

bfs()