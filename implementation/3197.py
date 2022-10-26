import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
R, C = map(int, input().split())
water_visit = [[False for _ in range(C)] for _ in range(R)]
bird_visit = [[False for _ in range(C)] for _ in range(R)]
lake = []
bird_location = []
water_queue = deque()
temp_water_queue = deque()
bird_queue = deque()
temp_bird_queue = deque()

for i in range(R):
    row = list(input().rstrip())
    lake.append(row)
    
    for j in range(C):
        if row[j]=='L':
            bird_location.append((i, j))
            water_queue.append((i, j))
        elif row[j]=='.':
            water_visit[i][j] = True
            water_queue.append((i, j))
            
start_x, start_y = bird_location[0]
end_x, end_y = bird_location[1]

bird_queue.append((start_x, start_y))
bird_visit[start_x][start_y] = True
lake[start_x][start_y] = '.'
lake[end_x][end_y] = '.'

def iceMelting(l):
    while water_queue:
        x, y = water_queue.popleft()
    
        if lake[x][y]=='X': lake[x][y] = '.'
    
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<R and 0<=ny<C:
             if not water_visit[nx][ny]:
                if l[nx][ny]=='X':
                    temp_water_queue.append((nx, ny))
                else: water_queue.append((nx, ny))
                water_visit[nx][ny] = True
                    
def isMeeting(l):
    while bird_queue:
        cx, cy = bird_queue.popleft()
        
        if cx==end_x and cy==end_y:
            return True
        
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<=nx<R and 0<=ny<C:
                if not bird_visit[nx][ny]:
                    if l[nx][ny]=='.':
                        bird_queue.append((nx, ny))
                    else: temp_bird_queue.append((nx, ny))
                    bird_visit[nx][ny] = True
    
    return False


turn = 0
while True:
    iceMelting(lake)
    
    if isMeeting(lake): break
    
    water_queue, bird_queue = temp_water_queue, temp_bird_queue
    temp_water_queue = deque()
    temp_bird_queue = deque()

    turn += 1

print(turn)