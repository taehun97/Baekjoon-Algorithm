import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def dfs(node, candidates):
    parent = getParent(node)
    if parent!=-1: 
        candidates.append(parent)
        dfs(parent, candidates)
        
def getParent(node):
    for (p, c) in connections:
        if c==node: return p
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    connections = [tuple(map(int, input().split())) for _ in range(n-1)]
    node = list(map(int, input().split()))
    
    parent_list = [[] for _ in range(2)]
    parent_list[0].append(node[0])
    parent_list[1].append(node[1])
    
    for i in range(2):
        dfs(node[i], parent_list[i])
        
    answer = 0
    for i in range(min(len(parent_list[0]), len(parent_list[1]))):
        if parent_list[0][-1-i]==parent_list[1][-1-i]:
            answer = parent_list[0][-1-i]
        
    print(answer)