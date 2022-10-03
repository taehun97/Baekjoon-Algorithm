import sys

input = sys.stdin.readline
answer = 0
m = []
path = [0]*26
d_x = [1, -1, 0, 0]
d_y = [0, 0, -1, 1]

r, c = map(int, input().split())
for _ in range(r):
    m.append(list(input().strip()))
    
def dfs(length, x, y):
    global answer
    answer = max(length, answer)
    
    for i in range(4):
        nx, ny = x + d_x[i], y + d_y[i]
        if 0<=nx<r and 0<=ny<c and path[ord(m[nx][ny])-65]==0:
            path[ord(m[nx][ny])-65] = 1
            dfs(length+1, nx, ny)
            path[ord(m[nx][ny])-65] = 0    

path[ord(m[0][0])-65] = 1
dfs(1, 0, 0)

print(answer)