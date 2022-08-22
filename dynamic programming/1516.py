import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cost = [0 for _ in range(n+1)]
adjacent = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for i in range(1, n+1):
    r = list(map(int, input().split()))[:-1]
    cost[i] = r[0]
    connections = r[1:]
    
    for c in connections:
        adjacent[c].append(i)
        indegree[i] += 1

def topologySort():
    q = deque()
    result = [0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        if indegree[i]==0: q.append(i)
        
    while q:
        now = q.popleft()
        
        result[now] += cost[now]
        for i in adjacent[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now])
            
            if indegree[i]==0: q.append(i)
            
    return result
        
answer = topologySort()

for i in range(1, n+1):
    print(answer[i])