import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = []
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
time = 0
exp = 0

for i in range(n):
    row = list(map(int, input().split()))
    maps.append(row)
    
    for j in range(n):
        if row[j]==9:
            maps[i][j] = 2
            start = [i, j]

def bfs(cur_x, cur_y):
    visited = [[False]*n for _ in range(n)]
    visited[cur_x][cur_y] = True
    eating_list = []
    dist = [[0]*n for _ in range(n)]
    q = deque()
    q.append([cur_x, cur_y])
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            new_x, new_y = x + d[k][0], y + d[k][1]
            if 0<=new_x<n and 0<=new_y<n and not visited[new_x][new_y]:
                if maps[new_x][new_y]<=maps[i][j] or maps[new_x][new_y]==0:
                    q.append([new_x, new_y])
                    visited[new_x][new_y] = True
                    dist[new_x] [new_y] = dist[x][y] + 1
                    
                if maps[new_x][new_y]<maps[i][j] and maps[new_x][new_y]!=0:
                    eating_list.append([new_x, new_y, dist[new_x][new_y]])
                    
    if not eating_list:
        return -1, -1, -1
    eating_list.sort(key = lambda x : (x[2], x[0], x[1]))
    return eating_list[0][0], eating_list[0][1], eating_list[0][2]                   
                
        
while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
             
    if ex==-1: break
    
    maps[ex][ey] = maps[i][j]
    maps[i][j] = 0
    start = [ex, ey]
    exp += 1
    
    if exp == maps[ex][ey]:
        maps[ex][ey] += 1
        exp = 0
    time += dist
    
print(time)