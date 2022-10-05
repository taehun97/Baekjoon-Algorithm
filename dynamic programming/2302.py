import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
vip_seat = [0] + []
for _ in range(M):
    vip_seat.append(int(input()))
vip_seat.append(N+1)

def getFibonacci(n):
    if n<=0: return 1
    
    dp = [1, 2] + [0 for _ in range(38)]
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

answer = 1
for i in range(1, M+2):
    num = vip_seat[i] - vip_seat[i-1] - 1
    answer *= getFibonacci(num)
    
print(answer)
    

    