N = int(input())

dp = [1] + [0 for _ in range(N)]
for i in range(1, N+1):
    if i%2==0: dp[i] = dp[i - 2] + dp[i // 2]
    else: dp[i] = dp[i - 1]  
          
print(dp[N]%1000000000)