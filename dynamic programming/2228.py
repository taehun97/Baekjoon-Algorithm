N, M = map(int, input().split())

dp = [[[0] +  [-1e9 for _ in range(M)] for _ in range(2)] for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min(M, (i+1)//2)+1):
        dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j])
        dp[i][1][j] = max(dp[i-1][0][j-1], dp[i-1][1][j]) + num

print(max(dp[N][0][M], dp[N][1][M]))