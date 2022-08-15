import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[a for a in input().rstrip()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def dfs(cnt, x, y, char, start_x, start_y):
    global isCycle
    
    if (x, y)==(start_x, start_y) and cnt>=4:
        print("Yes")
        exit()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0>nx or nx>=n or 0>ny or ny>=m or board[nx][ny]!=char: continue
        
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(cnt+1, nx, ny, board[nx][ny], start_x, start_y)
            visited[nx][ny] = False
                

for i in range(n):
    for j in range(m):
        dfs(0, i, j, board[i][j], i, j)
print("No")