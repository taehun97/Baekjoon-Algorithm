import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    # 누적합의 시작점이 달라지는 지점을 파악해야 해결 가능!    
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    
print(max(dp))