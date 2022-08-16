import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
soil = [[5 for _ in range(n)] for _ in range(n)]
nutrition = [list(map(int, input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
dead_trees = []

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
    
def spring():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                t = 0
                while t<len(trees[i][j]):
                    if trees[i][j][t]<=soil[i][j]:
                        soil[i][j] -= trees[i][j][t]
                        trees[i][j][t] += 1
                        t += 1
                    else:
                        d_tree = trees[i][j].pop(t)
                        dead_trees.append((i, j, d_tree))
                        
def summer():
    while dead_trees:
        x, y, n = dead_trees.pop()
        soil[x][y] += n//2
        
def autumn():
    childrens = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            for t in trees[i][j]:             
                if t%5==0: childrens.append((i, j))
                
    for x, y in childrens:
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<n and 0<=ny<n: trees[nx][ny].append(1)
            
def winter():
    for i in range(n):
        for j in range(n):
            soil[i][j] += nutrition[i][j]

def treeCounting():
    result = 0
    
    for i in range(n):
        for j in range(n):
            result += len(trees[i][j])
            
    return result
            
for time in range(k):
    spring()
    summer()
    autumn()
    winter()
    
print(treeCounting())
    
