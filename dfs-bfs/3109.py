import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maps = []
paths = []
visited = [[False]*c for _ in range(r)]
max_pipeline = 0
d_x = [-1, 0, 1]

def dfs(x, y):
    
    if y==c-1:
        return True
    
    for i in range(3):
        nx, ny = x + d_x[i], y + 1
        if 0<=nx<r and 0<=ny<c and maps[nx][ny]!='x' and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False

for _ in range(r):
    row = list(input())
    maps.append(row)
    
for i in range(r):
    if maps[i][0]=='.':
        if dfs(i, 0):
            max_pipeline += 1
            
print(max_pipeline)