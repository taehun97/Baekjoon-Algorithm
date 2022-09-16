import sys

input = sys.stdin.readline

n = int(input())
ary = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
cumulative_ary = [[]] + [[ary[x]] for x in range(1, n+1)]

for i in range(1, n+1):
    idx = 0
    max_dp = 0
    for j in range(i-1, -1, -1):
        if ary[i]>ary[j] and max_dp<dp[j]:
                max_dp = dp[j]
                idx = j
    
    dp[i] = max_dp + 1
    cumulative_ary[i] = cumulative_ary[idx] + cumulative_ary[i]
    
print(max(dp))
x = dp.index(max(dp))
print(' '.join(map(str, cumulative_ary[x])))