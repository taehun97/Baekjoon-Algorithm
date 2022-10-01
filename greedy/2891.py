from os import stat
import sys

input = sys.stdin.readline

n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
surplus = list(map(int, input().split()))

status = [1 for _ in range(n)]
for d in damaged:
    status[d-1] -= 1
for s in surplus:
    status[s-1] += 1
    
for i in range(n):
    if status[i]==2:      
        if i==0:
            if status[i+1]==0:
                status[i] = 1
                status[i+1] = 1
        elif i==n-1:
            if status[i-1]==0:
                status[i] = 1
                status[i-1] = 1
        else:
            if status[i-1]==0:
                status[i] = 1
                status[i-1] = 1
                
            if status[i+1]==0 and status[i]==2:
                status[i] = 1
                status[i+1] = 1
      
answer = 0
for i in range(n):
    if status[i]==0: answer += 1
    
print(answer)