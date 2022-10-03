import sys
from collections import deque

input = sys.stdin.readline

def bfs(idx):
    q = deque()
    isTree = True
    q.append(idx)
    
    while q:
        n = q.popleft()
        
        if visited[n]: isTree = False
        
        visited[n] = True
        for node in info[n]:
            if not visited[node]:
                q.append(node)
                
    return isTree

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n==0 and m==0: break
    
    info = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    answer = 0

    
    for _ in range(m):
        a, b = map(int, input().split())
        info[a].append(b)
        info[b].append(a)
        
    for i in range(1, n+1):
        if not visited[i]:
            if bfs(i): answer += 1
            
    if answer==0:
        print("Case {}: No trees.".format(case))
    elif answer==1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, answer))
        
        