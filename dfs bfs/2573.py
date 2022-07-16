import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

x, y = map(int, input().split())
maps = []
years = 0
d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

def dfs(v, cx, cy):
    v[cx][cy] = 1        
    for i in range(4):
        nx, ny = cx + d_x[i], cy + d_y[i]
        if 0<=nx<x and 0<=ny<y and maps[nx][ny]>0 and v[nx][ny]==0:
            dfs(v, nx, ny)

def melt():
    for i in range(x):
        for j in range(y):
            if maps[i][j]==0: continue
            
            water_grid = 0
            for k in range(4):
                nx, ny = i + d_x[k], j + d_y[k]
                if 0<=nx<x and 0<=ny<y and isVisited[nx][ny]==0:
                    water_grid += 1
            
            melting_list.append((i, j, water_grid))
        
    
for i in range(x):
    row = list(map(int, input().split()))
    maps.append(row)
    
chunks = 0
year = 0
glacier_count = 1
    
while chunks<2 and glacier_count>0:
    chunks = 0
    glacier_count = 0
    isVisited = [[0]*y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if isVisited[i][j]==0 and maps[i][j]>0:
                glacier_count += 1
                dfs(isVisited, i, j)
                chunks += 1
                
    if chunks>1: 
        break
    
    melting_list=[]
    melt()
    while melting_list:
        a, b, area = melting_list.pop()
        if maps[a][b]<=area:
            maps[a][b]=0
        else:
            maps[a][b] -= area
        
    years += 1
    
print(years)