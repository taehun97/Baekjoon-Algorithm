import sys
from collections import deque

input = sys.stdin.readline

def checkLeft(start, d):
    if start<1 or gears[start+1][6]==gears[start][2]:
        return
    
    if gears[start+1][6]!=gears[start][2]:
        checkLeft(start-1, -d)
        gears[start].rotate(d)
    
def checkRight(end, d):
    if end>4 or gears[end-1][2]==gears[end][6]:
        return
    
    if gears[end-1][2]!=gears[end][6]:
        checkRight(end+1, -d)
        gears[end].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, list(input().replace('\n', '')))))
    
n = int(input())

for i in range(n):
    num, direction = map(int, input().split())
    
    checkRight(num+1, -direction) 
    checkLeft(num-1, -direction)

    gears[num].rotate(direction)
    
result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0]
    
print(result)