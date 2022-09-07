import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
durability = list(map(int, input().split()))
belt = deque([[0, i] for i in durability]) # 0 => robot X | 1 => robot O

def isDurable():
    cnt = 0
    for b in belt:
        if b[1]==0: cnt += 1
        
    return True if cnt<k else False

step = 0
while isDurable():
    step += 1
    
    # phase 1
    belt.rotate(1)
    belt[n-1][0] = 0
    
    # phase 2
    for i in range(n-2, -1, -1):
        if belt[i][0]==1 and belt[i+1][0]==0 and belt[i+1][1]>0:
            belt[i][0] = 0
            belt[i+1][0] = 1
            belt[i+1][1] -= 1
    belt[n-1][0] = 0
    
    # phase 3
    if belt[0][0]==0 and belt[0][1]>0:
        belt[0][0] = 1
        belt[0][1] -= 1
        
print(step)
