import sys

input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    max_dp = 0
    for j in range(i, -1, -1):
        if box[i]>box[j]: max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1
    
print(max(dp))