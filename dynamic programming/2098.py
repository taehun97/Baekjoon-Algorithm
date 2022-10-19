import sys

input = sys.stdin.readline

N = int(input())
INF = 10e9

distance = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(1<<N-1)] for _ in range(N)]

def dfs(x, visit):
    if dp[x][visit]!=0:
        return dp[x][visit]
    
    if visit==(1<<(N-1))-1:
        if distance[x][0]:
            return distance[x][0]
        else:
            return INF
        
    min_route = INF
        
    for next in range(1, N):
        if not distance[x][next]:
            continue
        if visit&(1<<next-1):
            continue
        D = distance[x][next] + dfs(next, visit|(1<<(next-1)))
        
        if min_route>D: min_route = D
        
    dp[x][visit] = min_route

    return min_route

print(dfs(0, 0))