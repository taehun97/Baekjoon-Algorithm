import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i]>A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))