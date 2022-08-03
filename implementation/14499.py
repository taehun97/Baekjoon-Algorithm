import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if direction==1: # 동
        dice[0] = d; dice[1] = b; dice[2] = a; dice[3] = f; dice[4] = e; dice[5] = c
    elif direction==2: # 서
        dice[0] = c; dice[1] = b; dice[2] = f; dice[3] = a; dice[4] = e; dice[5] = d
    elif direction==3: # 북
        dice[0] = e; dice[1] = a; dice[2] = c; dice[3] = d; dice[4] = f; dice[5] = b
    else: # 남
        dice[0] = b; dice[1] = f; dice[2] = c; dice[3] = d; dice[4] = a; dice[5] = e

def updateDiceOrMap(cx, cy):
    if maps[cx][cy]==0:
        # 주사위 바닥면의 수 -> 칸
        maps[cx][cy] = dice[-1][1]
        
    else:
        # 칸의 수 -> 주사위의 바닥면
        dice[-1][1] = maps[cx][cy]
        maps[cx][cy] = 0

nx, ny = x, y        
for i in range(k):
    nx += dx[move[i] - 1]
    ny += dy[move[i] - 1]
    
    if nx<0 or nx>=n or ny<0 or ny>=m:
        nx -= dx[move[i] - 1]
        ny -= dy[move[i] - 1]
        continue
    
    turn(move[i])
    updateDiceOrMap(nx, ny)
    x, y = nx, ny
    print(dice[0][1])


    
    