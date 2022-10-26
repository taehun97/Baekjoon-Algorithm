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
        
        print(cx, cy)
        
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
    
    print("Turn: " + str(turn))
    for row in lake:
        print(*row)
    print()
    
    if isMeeting(lake): break
    
    print(water_queue)
    print(bird_queue)
    print(temp_water_queue)
    print(temp_bird_queue)
    
    water_queue, bird_queue = temp_water_queue, temp_bird_queue
    temp_water_queue = deque()
    temp_bird_queue = deque()

    print(water_queue)
    print(bird_queue)
    print(temp_water_queue)
    print(temp_bird_queue)

    turn += 1

print(turn)

# from collections import deque
# import sys

# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs():
#     while q:
#         x, y = q.popleft()
#         if x == x2 and y == y2:
#             return 1
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if not c[nx][ny]:
#                     if a[nx][ny] == '.':
#                         q.append([nx, ny])
#                     else:
#                         q_temp.append([nx, ny])
#                     c[nx][ny] = 1
#     return 0

# def melt():
#     while wq:
#         x, y = wq.popleft()
#         if a[x][y] == 'X':
#             a[x][y] = '.'
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if not wc[nx][ny]:
#                     if a[nx][ny] == 'X':
#                         wq_temp.append([nx, ny])
#                     else:
#                         wq.append([nx, ny])
#                     wc[nx][ny] = 1

# m, n = map(int, input().split())
# c = [[0]*n for _ in range(m)]
# wc = [[0]*n for _ in range(m)]

# a, swan = [], []
# q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

# for i in range(m):
#     row = list(input().strip())
#     a.append(row)
#     for j, k in enumerate(row):
#         if a[i][j] == 'L':
#             swan.extend([i, j])
#             wq.append([i, j])
#         elif a[i][j] == '.':
#             wc[i][j] = 1
#             wq.append([i, j])

# x1, y1, x2, y2 = swan
# q.append([x1, y1])
# a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
# cnt = 0

# while True:
#     melt()
#     if bfs():
#         print(cnt)
#         break
#     q, wq = q_temp, wq_temp
#     q_temp, wq_temp = deque(), deque()
#     cnt += 1