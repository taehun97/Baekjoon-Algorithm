import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(h)]

if m==0:
    print(0)
    exit(0)

for _ in range(m):
    a, b = map(int, input().split())
    visited[a-1][b-1] = True
    
answer = 4

def dfs(cnt, x, y):
    global answer
    
    if check():
        answer = min(answer, cnt)
        return
    elif cnt==3 or answer<=cnt: return
    
    for i in range(x, h):
        if x==i: k = y
        else: k = 0
        for j in range(k, n-1):
            if not visited[i][j] and not visited[i][j+1]:
                if j>0 and visited[i][j-1]: continue
                
                visited[i][j] = True
                dfs(cnt+1, i, j+2)
                visited[i][j] = False

def check():
    for start in range(n):
        k = start
        for j in range(h):
            if visited[j][k]: k += 1
            elif k>0 and visited[j][k-1]: k -= 1
        if k!=start: return False        
    return True


    
dfs(0, 0, 0) # argument: cnt, x, y
print(answer if answer<4 else -1)