N = int(input())
number = list(map(int, input().split()))

temp = [[0 for _ in range(N)] for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(0, N):
    for j in range(i, N):
        temp[i][j] = max(number[i:j+1]) - min(number[i:j+1])
    
for i in range(1, N):
    dp[i] = temp[0][i]
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + temp[i-j+1][i])
    
print(dp[-1])