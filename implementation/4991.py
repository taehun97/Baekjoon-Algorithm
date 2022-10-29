import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, d_coords, h, w, b):
    v = [[[float('inf') for _ in range(w)] for _ in range(h)] for _ in range(2**len(dust_coords)+1)]
    queue = deque()
    queue.append((x, y, 0, 0, 0))
    d_len = len(d_coords)
    answer = float('inf')
    
    while queue:
        cx, cy, cnt, time, dirty_status = queue.popleft()
        
        if cnt==d_len:
            answer = min(answer, time)
            
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<=nx<h and 0<=ny<w:
                if b[nx][ny]=='.' or b[nx][ny]=='o':
                    if v[dirty_status][nx][ny]>time + 1:
                        v[dirty_status][nx][ny] = time + 1
                        queue.append((nx, ny, cnt, time + 1, dirty_status))
                elif b[nx][ny]=='*':
                    if dirty_status & 2 ** (d_coords.index((nx, ny)))==0:
                        v[dirty_status][nx][ny] = time + 1
                        new_dirty_status = dirty_status | 2 ** (d_coords.index((nx, ny)))
                        queue.append((nx, ny, cnt + 1, time + 1, new_dirty_status))
                    else:
                        if v[dirty_status][nx][ny]>time + 1:
                            v[dirty_status][nx][ny] = time + 1
                            queue.append((nx, ny, cnt, time + 1, dirty_status))
                            
    if answer==float('inf'): return -1
    else: return answer
                    

answer_list = [] 
while True:
    w, h = map(int, input().split())
    robot_x, robot_y = -1, -1
    dust_coords = []
    
    if w==0 and h==0: break
    
    board = []
    for i in range(h):
        row = list(input().rstrip())
        board.append(row)
        
        for j in range(w):
            if row[j]=='o': robot_x, robot_y = i, j
            elif row[j]=='*': dust_coords.append((i, j))
    

    answer = bfs(robot_x, robot_y, dust_coords, h, w, board)
    answer_list.append(answer)
        
for e in answer_list:
    print(e)