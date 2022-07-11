n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range (k+1)]
for i in range(n+1):
    dp[1][i] = 1
    
for i in range(2, k+1):
    dp[i][0] = 1
    
for i in range(2, k+1):
    for j in range(1, n+1):
        for k in range(0, j+1):
            dp[i][j] += dp[i-1][j-k]
        dp[i][j] = dp[i][j]
    
print(dp[-1][-1]%1000000000)