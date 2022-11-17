import sys

input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(2)] for _ in range(N)]

if N==1:
    print(1)
    exit()

dp[0][0] = 0
dp[0][1] = 1

dp[1][0] = dp[0][1] + dp[0][0]
dp[1][1] = 0

for i in range(2, N):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]
    
print(sum(dp[N-1]))