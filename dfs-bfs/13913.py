import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
prev = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]

def path(node):
    result = []
    temp = node
    for _ in range(dist[node]+1):
        result.append(temp)
        temp = prev[temp]
    return result[::-1]

def bfs(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        cur_location = queue.popleft()

        if cur_location==K:
            return path(cur_location)
        
        for next_location in [cur_location+1, cur_location-1, cur_location*2]:
            if 0<=next_location<=100000 and dist[next_location]==0:
                dist[next_location] = dist[cur_location] + 1
                prev[next_location] = cur_location
                queue.append(next_location)

r = bfs(N)
print(len(r) - 1)
for e in r:
    print(e, end = ' ')
