import sys

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 1: up 2: down 3: left 4: right
N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s_direction = [0] + list(map(int, input().split()))

d_priority = [[] for _ in range(M+1)]
for i in range(1, M+1):
    d_priority[i].append([])
    for _ in range(4):
        d_priority[i].append(list(map(int, input().split())))
    
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

def isOnlyOneShark(n, b):
    for i in range(n):
        for j in range(n):
            if b[i][j]!=0 and b[i][j]!=1:
                return False
    return True

def spreadSmell(n, b, s, k):
    for i in range(n):
        for j in range(n):
            if b[i][j]!=0:
                s[i][j][0] = b[i][j]
                s[i][j][1] = k
                
def decideNextLocations(n, b, s):
    result = [[-1, -1, -1] for _ in range(M+1)]
    
    for i in range(n):
        for j in range(n):
            if b[i][j]!=0:
                # check blank block
                shark_number = b[i][j]
                direction = s_direction[shark_number]
                priority = d_priority[shark_number][direction]
                blankFlag = False
                
                # print(shark_number)
                # print(priority)
                
                for p in priority:
                    nx, ny = i + dx[p], j + dy[p]
                    if 0<=nx<n and 0<=ny<n and b[nx][ny]==0 and s[nx][ny][0]==0:
                        result[shark_number][0] = nx
                        result[shark_number][1] = ny
                        result[shark_number][2] = p
                        blankFlag = True
                        break
                        
                if blankFlag: continue
                
                # check smell block    
                for p in priority:
                    nx, ny = i + dx[p], j + dy[p]
                    if 0<=nx<n and 0<=ny<n and b[nx][ny]==0 and s[nx][ny][0]==shark_number:
                        result[shark_number][0] = nx
                        result[shark_number][1] = ny
                        result[shark_number][2] = p
                        break
                    
    return result
                        
def deleteSmallerShark(next_location_list, m):
    for i in range(1, m+1):
        bnx, bny, bnd = next_location_list[i]
        if bnx==-1 and bny==-1 and bnd==-1: continue
        for j in range(i+1, m+1):
            snx, sny, snd = next_location_list[j]
            if snx==-1 and sny==-1 and snd==-1: continue
            
            if bnx==snx and bny==sny:
                next_location_list[j][0] = -1
                next_location_list[j][1] = -1
                next_location_list[j][2] = -1
                
    return next_location_list

def moveSharks(n, m, b, s_d, next_location_list):
    for i in range(n):
        for j in range(n):
            if b[i][j]!=0: b[i][j] = 0
            
    for i in range(1, m+1):
        nx, ny, nd = next_location_list[i]
        if nx==-1 and ny==-1 and nd==-1: continue
        
        b[nx][ny] = i
        s_d[i] = nd
        
def decrementSmells(n, b, s):
    for i in range(n):
        for j in range(n):
            if s[i][j][0]==0 and s[i][j][1]==0: continue
            
            s[i][j][1] -= 1
            if s[i][j][1]==0: s[i][j][0] = 0
    
time = 0  
while not isOnlyOneShark(N, board):

    spreadSmell(N, board, smell, k)

    nll = decideNextLocations(N, board, smell)
    
    # print(nll)

    nll = deleteSmallerShark(nll, M)
    
    decrementSmells(N, board, smell)
    
    moveSharks(N, M, board, s_direction, nll)
    

    
    time += 1
    
    # print()
    # for row in board:
    #     print(*row)
    # print()
    
    # for row in smell:
    #     print(*row)
    # print()
    
    if time>1000:
        print(-1)
        exit()
    
print(time)
    
    
