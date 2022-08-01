import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    
    isError = False
    functions = list(input().rstrip())
    cnt = int(input())
    array = input().rstrip()[1:-1].split(',')
    queue = deque(array)
    
    rev, front, back = 0, 0, len(queue) - 1
    if cnt==0:
        queue = []
        front = 0
        back = 0
        
    for f in functions:
        if f=="R":
            rev += 1
            
        elif f=="D":
            if len(queue)<1:
                isError = True
                print("error")
                break
            else:
                if rev%2==0:
                    queue.popleft()
                else:
                    queue.pop()
                    
    if not isError:
        if rev%2==1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
                