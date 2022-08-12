import sys
import copy

input = sys.stdin.readline

r, c, t = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
up = -1
down = -1

def dustSpreading(h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    spread = copy.deepcopy(h)
    
    for i in range(r):
        for j in range(c):
            if spread[i][j]!=-1 and spread[i][j]!=0:
                spread[i][j] = spread[i][j]//5
                
    for i in range(r):
        for j in range(c):
            if h[i][j]!=-1:
                direction_cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0<=nx<r and 0<=ny<c and spread[nx][ny]!=-1:
                        direction_cnt += 1
                        h[i][j] += spread[nx][ny]
                h[i][j] -= spread[i][j]*direction_cnt

# 공기청정기 위쪽 이동
def airUp(h):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        h[x][y], before = before, h[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def airDown(h):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        h[x][y], before = before, h[x][y]
        x = nx
        y = ny 

    
    
def getDustQuantity(h):
    result = 0
    
    for i in range(r):
        for j in range(c):
            if h[i][j]>0:
                result += h[i][j]
                
    return result


for i in range(r):
    if house[i][0]==-1:
        up = i
        down = i + 1
        break
            
for _ in range(t):
    dustSpreading(house)
    airUp(house)
    airDown(house)
    
print(getDustQuantity(house))