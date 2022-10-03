from collections import deque
import sys

r=sys.stdin.readline
edge=[]

N, M, V_start=map(int, r().split())
graph=[[] for _ in range (N+1)]
visited=[False]*(N+1)

for _ in range (M):
    v1, v2=map(int, r().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
for i in range (1, N+1):
    graph[i].sort()

def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v]=True
    queue=deque([v])
    while queue:
        v1=queue.popleft()
        print(v1, end=' ')
        for i in graph[v1]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
        
dfs(V_start)
print()

# initialize visited log
visited=[False]*(N+1)      
    
bfs(V_start)