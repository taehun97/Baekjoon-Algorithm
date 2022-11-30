import sys

input = sys.stdin.readline

N = int(input())
edges = []
for i in range(N):
    x, y, z = map(int, input().split())
    edges.append((x, y, z, i))
    
vertices = []
for j in range(3):
    edges.sort(key = lambda p : p[j])
    for i in range(1, N):
        vertices.append((abs(edges[i][j] - edges[i-1][j]), edges[i][3], edges[i-1][3]))
        
vertices.sort()

parent = [i for i in range(N)]

def findParent(parent, a):
    if parent[a]!=a:
        parent[a] = findParent(parent, parent[a])
    return parent[a]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a

ans = 0
for c, e1, e2 in vertices:
    if findParent(parent, e1)!=findParent(parent, e2):
        unionParent(parent, e1, e2)
        ans += c
print(ans)
    