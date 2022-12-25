import sys

input = sys.stdin.readline

N = int(input())
dp = [[float('inf'), -1] for _ in range(1000001)]

dp[1][0] = 0
for i in range(1, N+1):
    for j in [i+1, i*2, i*3]:
        if j<=1000000 and dp[i][0]+1<dp[j][0]:
            dp[j][0] = dp[i][0] + 1
            dp[j][1] = i
        
print(dp[N][0])
start = N

while start!=1:
    print(start, end=' ')
    start = dp[start][1]
print(1)