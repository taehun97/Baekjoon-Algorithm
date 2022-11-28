import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent[i] = i

graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))
    
graph.sort()

def findParent(parent, x):
    if x!=parent[x]:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a
    
answer = 0
info = []
for cost, e1, e2 in graph:
    if findParent(parent, e1)!=findParent(parent, e2):
        unionParent(parent, e1, e2)
        answer += cost
        info.append((-cost, e1, e2))
info.sort()
        
answer += info[0][0]
        
print(answer)
    