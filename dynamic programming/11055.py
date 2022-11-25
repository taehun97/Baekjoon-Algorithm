import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    temp = 0
    for j in range(i-1, -1, -1):
        if A[j]<A[i]:
            temp = max(temp, dp[j])
    dp[i] = temp + A[i]
    
print(max(dp))