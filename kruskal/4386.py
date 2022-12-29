import sys

input = sys.stdin.readline

def findParent(parent, x):
    if x!=parent[x]:
        x = findParent(parent, parent[x])
    return parent[x]

def parentUnion(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a

N = int(input())
stars = []
for _ in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))
    
graph = []
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        graph.append((c, i, j))
graph.sort()

parent = [0 for _ in range(N)]
for i in range(N):
    parent[i] = i
    
ans = 0
for cost, e1, e2 in graph:
    if findParent(parent, e1)!=findParent(parent, e2):
        parentUnion(parent, e1, e2)
        ans += cost
        
print("%.2f" %(ans))