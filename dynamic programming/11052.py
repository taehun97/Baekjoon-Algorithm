import sys

input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

dp[1] = P[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-k] + P[k] for k in range(1, i+1))
    
print(dp[N])