import sys
input = sys.stdin.readline

def dfs(r, c, cur):
    if len(c)==5:
        print(1)
        exit()
    
    for i in r[cur]:
        if i not in c:
            c.append(i)
            dfs(r, c, i)
            del c[-1]
    

n, m = map(int, input().split())
relation = [[] for _ in range(n)]
check = []

for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

for i in range(n):
    check.append(i)
    dfs(relation, check, i)
    del check[-1]
        
print(0)