import sys

input = sys.stdin.readline

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

test_case = int(input())
max_num = 0
for _ in range(test_case):
    n = int(input())

    if max_num<n:
        for i in range(max_num+1, n+1):
            if dp[i]!=0: continue
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
        max_num = n
    print(dp[n]) 