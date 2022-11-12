import sys

input = sys.stdin.readline
MOD = 1000000003

N = int(input())
K = int(input())

# dp[i][j] => i개의 색깔 중에서 j개를 선택한 경우의 수
dp = [([1] + [0 for _ in range(K)]) for _ in range(N+1)]

dp[1][1] = 1

for i in range(2, N+1):
    for j in range(1, K+1):
        if i==N:
            dp[i][j] = dp[i-1][j] + dp[i-3][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
            
        dp[i][j]%=MOD
            
print(dp[N][K])