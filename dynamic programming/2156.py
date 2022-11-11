import sys

input = sys.stdin.readline

n = int(input())
cost = []
for _ in range(n):
    cost.append(int(input()))
    
dp = [[0 for _ in range(3)] for _ in range(n)]

if n>=1: dp[0][0] = cost[0]

if n>=2:
    dp[1][0] = cost[1]
    dp[1][1] = cost[0] + cost[1]

if n>=3:
    dp[2][0] = cost[0] + cost[2]
    dp[2][1] = cost[1] + cost[2]
    dp[2][2] = cost[0] + cost[1]

    for i in range(3, n):
        dp[i][0] = max(dp[i-2]) + cost[i]
        dp[i][1] = max(dp[i-3]) + cost[i-1] + cost[i]
        dp[i][2] = dp[i-1][1]
    
print(max(dp[n-1]))