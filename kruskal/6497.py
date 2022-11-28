import sys

input = sys.stdin.readline

def findParent(parent, x):
    if x!=parent[x]:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a

while True:
    m, n = map(int, input().split())
    
    if m==0 and n==0: break

    vertices = []
    total_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        total_cost += z
        vertices.append((z, x, y))
        
    vertices.sort()
    
    parent = [i for i in range(m+1)]
    
    necessary_cost = 0
    for cost, e1, e2 in vertices:
        if findParent(parent, e1)!=findParent(parent, e2):
            unionParent(parent, e1, e2)
            necessary_cost += cost
            
    print(total_cost - necessary_cost)