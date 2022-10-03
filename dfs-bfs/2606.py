import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
visited = [0 for _ in range(101)]
connection_info = [[] for _ in range(101)]
pair = int(input())
for _ in range(pair):
    a, b = map(int, input().split())
    connection_info[a].append(b)
    connection_info[b].append(a)
    
def bfs(num):
    queue = deque()
    queue.append(num)
    visited[num] = 1
    
    while queue:
        cur_comp = queue.popleft()
        for comp in connection_info[cur_comp]:
            if visited[comp]==0:
                visited[comp] = 1
                queue.append(comp)
    
bfs(1)
print(sum(visited) - 1)
