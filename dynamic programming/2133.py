import sys

input = sys.stdin.readline

n = int(input())
dp = [1] + [0 for _ in range(n)]

for i in range(2, n+1, 2):
    if i==2: dp[i] = dp[i-2]*3
    else: dp[i] = dp[i-4]*2 + dp[i-2]*3
    
print(dp[n])