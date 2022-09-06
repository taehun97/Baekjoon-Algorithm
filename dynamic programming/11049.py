import sys

input = sys.stdin.readline

n = int(input())
array_info = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + array_info[j][0] * array_info[k][1] * array_info[x][1])
            
print(dp[0][n-1])