import sys
from collections import deque

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    count = arr.pop(0)
    
    if count==0:
        break

    stack = deque()    
    max_area = 0
    
    for i in range(count):
        while len(stack)!=0 and arr[stack[-1]]>arr[i]:
            idx = stack.pop()
            
            if len(stack)==0: width = i
            else: width = i - stack[-1] - 1
            
            max_area = max(max_area, width * arr[idx])
        stack.append(i)
        
    while len(stack)!=0:
        idx = stack.pop()
        
        if len(stack)==0: width = count
        else: width = count - stack[-1] - 1
        
        max_area = max(max_area, width * arr[idx])
        
    print(max_area)