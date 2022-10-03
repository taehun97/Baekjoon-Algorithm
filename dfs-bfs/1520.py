import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

M, N = map(int, input().split())
m = []
dp = [[-1 for _ in range(N)] for _ in range(M)]
direction_x=[1, -1, 0, 0]
direction_y=[0, 0, -1, 1]
for _ in range(M):
    m.append(list(map(int, input().split())))

def dfs(x, y):
    if x==M-1 and y==N-1:
        return 1
    
    if dp[x][y]!=-1:
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx, ny = x+direction_x[i], y+direction_y[i]
        if 0 <= nx < M and 0 <= ny < N and m[x][y]>m[nx][ny]:
            ways += dfs(nx, ny)
            
    dp[x][y] = ways
    return dp[x][y]

print(dfs(0, 0))