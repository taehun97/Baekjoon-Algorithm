import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        move = board[i][j]
        if move==0: break
        
        if 0<=i+move<N:
            dp[i+move][j] += dp[i][j]

        if 0<=j+move<N:
            dp[i][j+move] += dp[i][j]  
            
print(dp[N-1][N-1])
