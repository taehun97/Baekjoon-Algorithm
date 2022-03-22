# original
# i: memory
# dp[i]: minimal cost

# reverse
# i: cost
# dp[i]: maximum memory

import sys

r=sys.stdin.readline

N, M=map(int, r().split())
memory=[0]+list(map(int, r().split()))
cost=[0]+list(map(int, r().split()))
dp=[[0 for _ in range (sum(cost)+1)] for _ in range (N+1)]
min_cost=sum(cost)

for i in range (1, N+1):
    for j in range (1, sum(cost)+1):
        if j>=cost[i]:
            dp[i][j]=max(dp[i-1][j], memory[i]+dp[i-1][j-cost[i]])
        else: dp[i][j]=dp[i-1][j]
        
        if dp[i][j]>=M:
            min_cost=min(j, min_cost)

print(min_cost)