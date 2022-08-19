import sys
from heapq import heappush, heappop
from itertools import combinations

input = sys.stdin.readline

n, m, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
archer_list = [i for i in range(m)]
archer_combs = tuple(combinations(archer_list, 3))
ans = 0

def isBattleOver(f):
    for i in range(n):
        for j in range(m):
            if f[i][j]==1: return False
    return True

def killEnemy(f, index):
    global n, m, d
    count = 0
    
    attacked_enemy = []
    isAttacked = [[False for _ in range(m)] for _ in range(n)]
    
    for y in archer_combs[index]:
        heapq = []
        for i in range(n-1, -1, -1):
            for j in range(m):
                if f[i][j]==1:
                    distance = abs(y - j) + abs(i - n)
                    if distance<=d:
                        heappush(heapq, [distance, j, i]) # distance, j 순으로 자동 정렬
                        
        if heapq:
            _, y, x = heappop(heapq)
            attacked_enemy.append((y, x))        
                        
    for cy, cx in attacked_enemy:
        if not isAttacked[cx][cy]:
            isAttacked[cx][cy] = True
            f[cx][cy] = 0
            count += 1
            
    return count
            

def moveEnemy(f):
    global n, m
    
    f[-1] = [0 for _ in range(m)]
    for i in range(n-2, -1, -1):
        f[i+1] = f[i]
    f[0] = [0 for _ in range(m)]

def solve(idx):
    global temp_field
    count = 0
    
    while not isBattleOver(temp_field):
        count += killEnemy(temp_field, idx)
        
        moveEnemy(temp_field)

    return count

for i in range(len(archer_combs)):
    temp_field = [[field[i][j] for j in range(m)] for i in range(n)]
    cnt = solve(i)
    ans = max(ans, cnt)
    
print(ans)