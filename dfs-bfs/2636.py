import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

x, y = map(int, input().split())
maps = []
melting_list = []
cheeze_areas = []
d_x = [1, -1, 0, 0]
d_y = [0, 0, -1, 1]
year = 0

def isCheezeGone():
    isGone = True
    cheezeArea = 0
    
    for i in range(x):
        for j in range(y):
            if maps[i][j]==1:
                isGone = False
                cheezeArea += 1
    
    cheeze_areas.append(cheezeArea)
            
    return isGone

def dfs(cur_x, cur_y):
    visited[cur_x][cur_y] = 1
    
    if maps[cur_x][cur_y]==1: return
    
    for i in range(4):
        new_x, new_y = cur_x + d_x[i], cur_y + d_y[i]
        if 0<=new_x<x and 0<=new_y<y:
            if maps[new_x][new_y]==1 and (new_x, new_y) not in melting_list:
                melting_list.append((new_x, new_y))
            elif visited[new_x][new_y]==0: dfs(new_x, new_y)

def melt():
    while melting_list:
        m_x, m_y = melting_list.pop()
        maps[m_x][m_y] = 0

for _ in range(x):
    map_row = list(map(int, input().split()))
    maps.append(map_row)

while not isCheezeGone():
    visited = [[0 for _ in range(y)] for _ in range(x)]
        
    dfs(0, 0)
    melt()
    year += 1

print(year)
print(cheeze_areas[-2])