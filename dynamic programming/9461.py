import sys

input = sys.stdin.readline

T = int(input())
dp = [0, 1, 1] + [0 for _ in range(101)]

for _ in range(T):
    N = int(input())
    
    if dp[N]==0:
        for i in range(3, N+1):
            if dp[i]!=0: continue
            dp[i] = dp[i-2] + dp[i-3]
            
    print(dp[N])