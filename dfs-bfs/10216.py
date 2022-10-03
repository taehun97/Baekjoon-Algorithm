import sys

input = sys.stdin.readline

def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dfs(cur):
    for i in range(n):
        if distance(location[cur], location[i])>(location[cur][2] + location[i][2])**2 or i==cur or visited[i]:
            continue
        visited[i] = True
        dfs(i)

t = int(input())
for _ in range(t):
    n = int(input())
    location = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1
            
    print(answer)