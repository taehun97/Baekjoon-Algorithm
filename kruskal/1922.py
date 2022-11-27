import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
vertices = []
for _ in range(M):
    a, b, c = map(int, input().split())
    vertices.append((c, a, b))

parent = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent[i] = i
    
vertices.sort()

def findParent(parent, x):
    if parent[x]!=x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]
    
def unionParent(a, b, parent):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a>b: parent[a] = b
    else: parent[b] = a
    
answer = 0
for cost, e1, e2 in vertices:
    if findParent(parent, e1)!=findParent(parent, e2):
        unionParent(e1, e2, parent)
        answer += cost
    
print(answer)