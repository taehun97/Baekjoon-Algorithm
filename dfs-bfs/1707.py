import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

k = int(input())

def dfs(start, id):
    global result
    
    if result:
        return
    
    visited[start] = id
    
    for i in maps[start]:
        if visited[i]==0:
            dfs(i, -id)
            
        elif visited[start]==visited[i]:
            result = True
            return

for _ in range(k):
    v, e = map(int, input().split())
    
    maps = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    result = False
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        maps[v1].append(v2)
        maps[v2].append(v1)
        
    for i in range(1, v+1):
        if visited[i]==0:
            dfs(i, 1)
            if result:
                break
            
    if result:
        print("NO")
    else:
        print("YES")