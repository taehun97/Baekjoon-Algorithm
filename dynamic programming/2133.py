import sys

input = sys.stdin.readline

n = int(input())
dp = [1] + [0 for _ in range(n)]

# dp[i] = 3 * dp[i-2] + 2 * (dp[i-4] + dp[i-6] + ... + dp[2] + dp[0])
for i in range(2, n+1, 2):
    dp[i] += 3*dp[i-2]
    for k in range(i-4, -1, -2):
        dp[i] += 2*dp[k]
    
print(dp[n])