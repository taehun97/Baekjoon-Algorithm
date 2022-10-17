N, M, K = map(int, input().split())

flight_info = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    flight_info[a][b] = max(flight_info[a][b], c)
    
for i in range(2, N+1):
    dp[i][2] = flight_info[1][i]

for i in range(2, N+1):
    for j in range(3, M+1):
        for k in range(1, i):
            if dp[k][j-1] and flight_info[k][i]:
                dp[i][j] = max(dp[i][j], flight_info[k][i] + dp[k][j-1])

print(max(dp[N]))