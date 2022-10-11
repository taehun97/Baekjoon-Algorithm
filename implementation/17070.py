import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# BFS Solution
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y, 0))
#     result = 0
    
#     while queue:
#         cx, cy, type = queue.popleft()
#         start, end = -1, -1
        
#         if cx==N-1 and cy==N-1:
#             result += 1
#             continue
        
#         if type==0: start, end = 0, 2
#         elif type==1: start, end = 0, 3
#         else: start, end = 1, 3

#         for i in range(start, end):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0<=nx<N and 0<=ny<N:
#                 if i==0 or i==2:
#                     if board[nx][ny]!=1:
#                         queue.append((nx, ny, i))
#                 else:
#                     if board[nx][ny]!=1 and board[nx-1][ny]!=1 and board[nx][ny-1]!=1:
#                         queue.append((nx, ny, i))

#     return result

# print(bfs(0, 1))

# DFS Solution
# result = 0
# def dfs(x, y, t):
#     global result

#     if x==N-1 and y==N-1:
#         result += 1
#         return
    
#     if t==0:
#         if y+1<N and board[x][y+1]==0: dfs(x, y + 1, 0)
#         if x+1<N and y+1<N:
#             if board[x+1][y]==0 and board[x][y+1]==0 and board[x+1][y+1]==0:
#                 dfs(x + 1, y + 1, 1)
#     elif t==1:
#         if y+1<N and board[x][y+1]==0: dfs(x, y + 1, 0)
#         if x+1<N and y+1<N:
#             if board[x+1][y]==0 and board[x][y+1]==0 and board[x+1][y+1]==0:
#                 dfs(x + 1, y + 1, 1)
#         if x+1<N and board[x+1][y]==0: dfs(x + 1, y, 2)
#     elif t==2:
#         if x+1<N and y+1<N:
#             if board[x+1][y]==0 and board[x][y+1]==0 and board[x+1][y+1]==0:
#                 dfs(x + 1, y + 1, 1)
#         if x+1<N and board[x+1][y]==0: dfs(x + 1, y, 2)

# dfs(0, 1, 0)
# print(result)

# DP Solution
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(N):
    for j in range(N):
        for k in range(3):
            if dp[k][i][j]==0: continue
            
            if k==0:
                if j+1<N and board[i][j+1]==0:
                    dp[0][i][j+1] += dp[k][i][j]
                if i+1<N and j+1<N:
                    if board[i+1][j+1]==0 and board[i+1][j]==0 and board[i][j+1]==0:
                        dp[1][i+1][j+1] += dp[k][i][j]
            elif k==1:
                if i+1<N and board[i+1][j]==0:
                    dp[2][i+1][j] += dp[k][i][j]
                if i+1<N and j+1<N:
                    if board[i+1][j+1]==0 and board[i+1][j]==0 and board[i][j+1]==0:
                        dp[1][i+1][j+1] += dp[k][i][j]  
                if j+1<N and board[i][j+1]==0:
                    dp[0][i][j+1] += dp[k][i][j] 
            elif k==2:
                if i+1<N and j+1<N:
                    if board[i+1][j+1]==0 and board[i+1][j]==0 and board[i][j+1]==0:
                        dp[1][i+1][j+1] += dp[k][i][j]
                if i+1<N and board[i+1][j]==0:
                    dp[2][i+1][j] += dp[k][i][j]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])