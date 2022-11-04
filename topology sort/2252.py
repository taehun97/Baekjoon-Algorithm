import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# graph = [[False for _ in range(N)] for _ in range(N)]
inDegree = [[] for _ in range(N)]
outDegree = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    # graph[A][B] = True
    outDegree[A-1].append(B-1)
    inDegree[B-1].append(A-1)
    
queue = deque()
for i in range(N):
    if len(inDegree[i])==0:
        queue.append(i)
        
while queue:
    node = queue.popleft()
    print(node + 1, end = ' ')
    
    for next_node in outDegree[node]:
        inDegree[next_node].remove(node)
        if len(inDegree[next_node])==0:
            queue.append(next_node)
            
    outDegree[node].clear()
    
    
    
    
