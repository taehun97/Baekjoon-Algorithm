import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark_location = [[-1, -1] for _ in range(M+1)]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    for j in range(N):
        if row[j]!=0:
            shark_location[row[j]][0] = i
            shark_location[row[j]][1] = j
            smell[i][j][0], smell[i][j][1] = row[j], K

direction = list(map(int, input().split()))
priority = [[] for _ in range(M+1)]

# 0: up, 1: down, 2: left, 3: right
for i in range(1, M+1):
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isOnlyOneShark():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]!=0:
                cnt += 1
                if cnt>1: return False
    return True

def dfs(x, y, v):
    v[x][y] = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<N and not v[nx][ny] and smell[nx][ny][0]==smell[x][y][0]:
            smell[nx][ny][1] -= 1
            if smell[nx][ny][1]==0: smell[nx][ny][0] = 0
            else: dfs(nx, ny, v)
    
time = 0
while not isOnlyOneShark() and time<=1000:
    for row in board:
        print(*row)
    print()
    for row in smell:
        print(*row)
    print()
        
    next_move_list = []
    for i in range(M):
        # Case 1: No smell
        next_location_candidates = []
        for d in range(4):
            nx, ny = shark_location[i][0] + dx[d], shark_location[i][1] + dy[d]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 and smell[nx][ny]==(0, 0):
                next_location_candidates.append((nx, ny))
     
        if len(next_location_candidates)>1:
            index = -1
            # for e in priority[i][direction[i] - 1]:
            for new_x, new_y in next_location_candidates:
                local_index = -1
                xd, yd = new_x - shark_location[i][0], new_y - shark_location[i][1]

                if xd==0: local_index = dy.index(yd) + 1
                elif yd==0: local_index = dx.index(xd) + 1
                
                index = min(index, priority[i].index(local_index))
                
            nx, ny = shark_location[i][0] + dx[priority[i][index]], shark_location[i][1] + dy[priority[i][index]]
            next_move_list.append([nx, ny])
        
        elif len(next_location_candidates)==1:
            nx, ny = next_location_candidates[0]
            next_move_list.append([nx, ny])

        else:
            # Case 2: My smell
            next_location_candidates2 = []
            for i in range(4):
                cx, cy = shark_location[i][0] + dx[i], shark_location[i][1] + dy[i]
                if 0<=cx<N and 0<=cy<N and smell[cx][cy][0]==i+1:
                    next_location_candidates2.append((cx, cy))
            
            if len(next_location_candidates2)>1:
                index = -1
                # for e in priority[i][direction[i] - 1]:
                for new_x, new_y in next_location_candidates2:
                    local_index = -1
                    xd, yd = new_x - shark_location[i][0], new_y - shark_location[i][1]

                    if xd==0: local_index = dy.index(yd) + 1
                    elif yd==0: local_index = dx.index(xd) + 1
                    
                    index = min(index, priority[i].index(local_index))
                    
                nx, ny = shark_location[i][0] + dx[priority[i][index]], shark_location[i][1] + dy[priority[i][index]]
                next_move_list.append([nx, ny])
                
            elif len(next_location_candidates2)==1:
                nx, ny = next_location_candidates2[0]
                next_move_list.append([nx, ny])
        
    for i in range(len(next_move_list)):
        nx, ny = next_move_list[i]
                                
        # change shark location
        board[shark_location[i][0]][shark_location[i][1]] = 0
        board[nx][ny] = max(i + 1, board[nx][ny])
        
        # change direction
        print("nx, ny: " + str(nx) + ", " + str(ny))
        print("sx, sy: " + str(shark_location[i][0]) + ", " + str(shark_location[i][0]))
        ndx, ndy = nx - shark_location[i][0], ny - shark_location[i][1]
        if ndx==0: direction[i] = dy.index(ndy) + 1
        else: direction[i] = dx.index(ndx) + 1
        
        # change shark location coordinates and smell status
        shark_location[i][0], shark_location[i][1] = nx, ny
        smell[nx][ny][0], smell[nx][ny][1] = max(i + 1, smell[nx][ny][0]) , K
        
        visited = [[False]*N for _ in range(N)]
        dfs(nx, ny, visited)
            
    time += 1
    
print(time) if time<=1000 else print(-1)