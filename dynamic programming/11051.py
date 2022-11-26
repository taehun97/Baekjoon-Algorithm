import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [1, 1] + [0 for _ in range(N-1)]

for i in range(2, N+1):
    dp[i] = dp[i-1] * i
    
print((dp[N]//(dp[K] * dp[N-K])) % 10007)