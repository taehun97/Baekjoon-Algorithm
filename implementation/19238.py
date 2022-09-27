import sys
from collections import deque

input = sys.stdin.readline

N, M, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp_x, temp_y = map(int, input().split())
start_x, start_y = temp_x - 1, temp_y - 1
guest_start_coord = []
guest_end_coord = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    guest_start_coord.append((sx-1, sy-1))
    guest_end_coord.append((ex-1, ey-1))

def findNearestGuest(b, sx, sy, coord, g):
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append((sx, sy, 0))
    visited[sx][sy] = True
    x, y, dist, idx = -1, -1, -1, -1
    guest_analysis = []
    
    while queue:
        cx, cy, distance = queue.popleft()
        
        if (cx, cy) in coord:
            # idx = coord.index((cx, cy))
            # coord.pop(idx)
            guest_analysis.append((distance, cx, cy))
            # x, y = cx, cy
            # dist = distance
            # break
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and b[nx][ny]!=1:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
                
    if len(guest_analysis)>0:            
        guest_analysis.sort()
        dist, x, y = guest_analysis[0]
        idx = coord.index((x, y))
        coord.pop(idx)
                
    return x, y, g - dist, idx

def findFastestPath(b, x, y, coord, g, idx):
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y, 0))
    new_sx, new_sy, dist = -1, -1, -1
    
    ex, ey = coord[idx]
    
    while queue:
        cx, cy, distance = queue.popleft()
        
        if (cx, cy)==(ex, ey):
            coord.pop(idx)
            new_sx, new_sy = cx, cy
            dist = distance
            break
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and b[nx][ny]!=1:
                visited[nx][ny] = True
                queue.append((nx, ny, distance+1))
    
    if g<dist: return new_sx, new_sy, -1
    else: return new_sx, new_sy, g + dist
    
while len(guest_start_coord)!=0 or len(guest_end_coord)!=0:
    x, y, G, index = findNearestGuest(board, start_x, start_y, guest_start_coord, G)
    
    if G<=0 or (x, y)==(-1, -1):
        print(-1)
        exit()
    
    start_x, start_y, G = findFastestPath(board, x, y, guest_end_coord, G, index)
    
    if G<=0 or (start_x, start_y)==(-1, -1):
        print(-1)
        exit()
        
print(G)