import sys
from collections import deque

input = sys.stdin.readline

temp = []
wall_coords = []
flag = False
num = -1
for i in range(8):
    row = list(input().rstrip())
    temp.append(row)
    
    for j in range(8):
        if row[j]=='#':
            if not flag:
                flag = True
                num = i
            wall_coords.append([i, j])

if num==-1: num = 7
board = [[['.' for _ in range(8)] for _ in range(8)] for _ in range(8 - num)]
    
for i in range(8-num):
    for j in range(len(wall_coords)):
        x, y = wall_coords[j]
        if 0<=x<8 and 0<=y<8: board[i][x][y] = '#'
        
        wall_coords[j][0] += 1

dx = [1, -1, 0, 0, 1, -1, 1, -1, 0]
dy = [0, 0, 1, -1, 1, -1, -1, 1, 0]

start_x, start_y = 7, 0

def solve(start_x, start_y):
    queue = deque([])
    next_queue = deque()
    queue.append((start_x, start_y))
    
    isPossible = True
    
    for i in range(8-num):
        if len(queue)==0:
            isPossible = False
            break
        
        while queue:
            cx, cy = queue.popleft()
            if board[i][cx][cy]=='.': next_queue.append((cx, cy))
            
        while next_queue:
            x, y = next_queue.popleft()
            
            for d in range(9):
                nx, ny = x + dx[d], y + dy[d]
                if 0<=nx<8 and 0<=ny<8 and board[i][nx][ny]=='.': queue.append((nx, ny))

    if len(queue)==0: isPossible = False

    if isPossible: return 1
    else: return 0         
            
answer = solve(start_x, start_y)
print(answer)