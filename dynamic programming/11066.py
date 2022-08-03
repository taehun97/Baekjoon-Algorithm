import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    file = [0] + list(map(int, input().split()))
    dp = [[0]*(N+1) for _ in range(N+1)]
    
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + file[i]
    
    for i in range(2, N+1):
        for j in range(1, N+2-i):
            dp[j][j+i-1] = min(dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)) + S[j+i-1] - S[j-1]
            
    print(dp[1][N])