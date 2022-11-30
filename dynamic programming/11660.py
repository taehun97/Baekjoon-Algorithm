import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = board[0][0]
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + board[0][i]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + board[i][0]
    
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i][j]
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    if x1>=1 and y1>=1:
        ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    elif not(x1>=1) and y1>=1:
        ans = dp[x2][y2] - dp[x2][y1-1]
    elif x1>=1 and not(y1>=1):
        ans = dp[x2][y2] - dp[x1-1][y2]
    else:
        ans = dp[x2][y2]
    
    print(ans)