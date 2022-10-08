import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    
    store_list = []
    for _ in range(N):
        store_x, store_y = map(int, input().split())
        store_list.append((store_x, store_y))
        
    dest_x, dest_y = map(int, input().split())
    
    visited = []
    queue = deque()
    queue.append((start_x, start_y))
    visited.append((start_x, start_y))
    reachable = False
    
    while queue:
        cx, cy = queue.popleft()
        
        if abs(dest_x - cx) + abs(dest_y - cy)<=1000:
            reachable = True
            break
        
        for sx, sy in store_list:
            if (sx, sy) not in visited:
                distance = abs(sx - cx) + abs(sy - cy)
                if distance<=1000:
                    queue.append((sx, sy))
                    visited.append((sx, sy))
                
    print("happy") if reachable else print("sad")
    