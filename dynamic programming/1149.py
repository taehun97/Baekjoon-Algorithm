import sys

input = sys.stdin.readline
COLOR = 3 # Red: 0 Green: 1 Blue: 2

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf') for _ in range(COLOR)] for _ in range(N)]

for i in range(COLOR):
    dp[0][i] = cost[0][i]

for i in range(1, N):
    for j in range(COLOR):
        dp[i][j] = min(dp[i-1][k] + cost[i][j] for k in range(COLOR) if k!=j)
        
print(min(dp[N-1]))