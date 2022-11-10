import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)] 
    
dp = [[0 for _ in range(i+1)] for i in range(n)]
for i in range(n):
    for j in range(len(dp[i])):
        if j==0:
            dp[i][j] = dp[i-1][j] + cost[i][j]
        elif j==len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1] + cost[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + cost[i][j]
            
print(max(dp[n-1]))