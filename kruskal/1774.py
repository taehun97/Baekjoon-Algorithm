import sys

input = sys.stdin.readline

N, M = map(int, input().split())

location = []
for _ in range(N):
    x, y = map(int, input().split())
    location.append((x, y))
    
graph = []
for i in range(N-1):
    for j in range(i+1, N):
        c = ((location[i][0] - location[j][0])**2 + (location[i][1] - location[j][1])**2)**(1/2)
        graph.append((c, i + 1, j + 1))
graph.sort()
    
parent = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent[i] = i

def findParent(parent, x):
    if parent[x]!=x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def parentUnion(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a

for _ in range(M):
    a, b = map(int, input().split())
    parentUnion(parent, a, b)
    
ans = 0
for cost, e1, e2 in graph:
    if findParent(parent, e1)!=findParent(parent, e2):
        parentUnion(parent, e1, e2)
        ans += cost
print('%.2f' %(ans))