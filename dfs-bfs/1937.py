import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
forest = []
longest_path = [[-1]*n for _ in range(n)]
d_x = [1, -1, 0, 0]
d_y = [0, 0, -1, 1]

for _ in range(n):
    forest.append(list(map(int, input().split())))



def dfs(x, y):
    choice = [0, 0, 0, 0]
    
    for d in range(4):
        nx, ny = x + d_x[d], y + d_y[d]
        if 0<=nx<n and 0<=ny<n and forest[x][y]<forest[nx][ny]:
            if longest_path[nx][ny]==-1:
                dfs(nx, ny)

            choice[d] = longest_path[nx][ny]
         
    longest_path[x][y] = max(choice) + 1

for i in range(n):
    for j in range(n):
        if longest_path[i][j]==-1:
            dfs(i, j)
        
max_path = 0
for element in longest_path:
    max_path = max(max_path, max(element))
    
print(max_path)