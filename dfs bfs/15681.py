import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, r, q = map(int, input().split())
connect = [[] for _ in range(n+1)]
children = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
size = [1 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
    
u = [int(input()) for _ in range(q)]
    
def makeTree(currentNode, p):
    for node in connect[currentNode]:
        if p!=node:
            children[currentNode].append(node)
            parent[node] = currentNode
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode):
    for node in children[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

makeTree(r, -1)
countSubtreeNodes(r)

for i in range(q):
    print(size[u[i]])