import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]
work_info = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    value = work_info[i][0]
    precedent_cnt = work_info[i][1]
    precedent_list = work_info[i][2:] if precedent_cnt>0 else []
    
    if precedent_cnt==0: dp[i] = value
    else: dp[i] = value + max(dp[k-1] for k in precedent_list)

print(max(dp))