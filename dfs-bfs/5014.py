import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F+1)]
direction = [U, -D]

queue = deque()
queue.append(S)
visited[S] = 0

while queue:
    cur = queue.popleft()
    for i in range(2):
        new = cur + direction[i]
        if 1<=new<=F and visited[new]==-1:
            visited[new] = visited[cur] + 1
            queue.append(new)
            
print("use the stairs") if visited[G]==-1 else print(visited[G])