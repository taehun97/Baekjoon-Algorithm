import sys

input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(1, n):
    maximum = 0
    for j in range(i-1, -1, -1):
        if num_list[i]>num_list[j] and maximum<dp[j]:
            maximum = dp[j]
    dp[i] += maximum
        
print(n -  max(dp))