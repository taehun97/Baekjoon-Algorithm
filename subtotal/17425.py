import sys

input = sys.stdin.readline

dp = [1 for _ in range(1000001)]
for i in range(2, 1000001):
    j = 1
    while i*j<=1000000:
        dp[i*j] += i
        j += 1

acumulative_sum = [0 for _ in range(1000001)]

for i in range(1, 1000001):
    acumulative_sum[i] = acumulative_sum[i-1] + dp[i]

T = int(input())

for _ in range(T):
    N = int(input())
    total_sum = 0
        
    print(acumulative_sum[N])