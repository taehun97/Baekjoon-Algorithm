from collections import deque

coordinate_queue=deque();

direction_x=[0, 0, 1, -1]
direction_y=[1, -1, 0, 0]
cnt=0;
cnt_blind=0;

def dfs(x, y):
    visited[x][y]=cnt
    coordinate_queue.append((x, y))
    while coordinate_queue:
        qx, qy=coordinate_queue.popleft()
        for i in range (4):
            nx=qx+direction_x[i]
            ny=qy+direction_y[i]
            if 0 <= nx < row_length and 0 <= ny < col_length:
                if visited[nx][ny]==0 and grid[qx][qy]==grid[nx][ny]:
                    coordinate_queue.append((nx, ny))
                    visited[nx][ny]=cnt


row_length=int(input())
col_length=row_length

grid=[['0']*col_length for a in range (row_length)]
visited=[[0]*col_length for a in range (row_length)]

# not color blind version
for i in range (row_length):
    col_str=input();
    for j in range (col_length):
        grid[i][j]=col_str[j];

for i in range (row_length):
    for j in range (col_length):
        if visited[i][j]==0:
            cnt+=1
            dfs(i, j)
        
# color blind version
for i in range (row_length):
    for j in range (col_length):
        visited[i][j]=0
        if grid[i][j]=="G":
            grid[i][j]="R"

for i in range (row_length):
    for j in range (col_length):
        if visited[i][j]==0:
            cnt_blind+=1
            dfs(i, j)

print(cnt, cnt_blind)






