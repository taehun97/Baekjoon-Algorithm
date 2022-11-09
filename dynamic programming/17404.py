import sys

input = sys.stdin.readline

RED, GREEN, BLUE = 0, 1, 2

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

answer = float('inf')    
for c in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]
    dp[0][c] = cost[0][c]
    
    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
                            
    for j in range(3):
        if c!=j:
            answer = min(answer, dp[N-1][j])
            
print(answer)