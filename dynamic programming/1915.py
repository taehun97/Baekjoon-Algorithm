import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    dp[i][0] = 1 if board[i][0]==1 else 0
    
for i in range(m):
    dp[0][i] = 1 if board[0][i]==1 else 0

for i in range(1, n):
    for j in range(1, m):
        if board[i][j]==1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

ans = 0
for i in range(n):
    local_ans = max(dp[i])
    ans = max(ans, local_ans)
print(ans**2)                
            