# not solved yet
from collections import deque

coordinate_queue=deque()
coordinate_x=[1, -1, 0, 0]
coordinate_y=[0, 0, 1, -1]

first_input=input()
m=int(first_input.split(' ')[0])
n=int(first_input.split(' ')[1])
k=int(first_input.split(' ')[2])

cnt=0;
grid=[[0]*n for i in range (m)]
coordinate=[[0]*4 for i in range (k)]
area=[1 for i in range (k)]

def dfs(x, y):
    grid[x][y]=area[cnt-1]
    coordinate_queue.append((x, y))
    while coordinate_queue:
        qx, qy=coordinate_queue.popleft()
        for a in range (4):
            nx=qx+coordinate_x[a]
            ny=qy+coordinate_y[a]
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny]==0:
                    area[cnt-1]+=1
                    coordinate_queue.append((nx, ny))
                    grid[nx][ny]=area[cnt-1]

def sort(arr):
    for i in range (0, len(arr)-1):
        for j in range (i+1, len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

for i in range (k):
    coordinate_str=input()
    coordinate_split=coordinate_str.split(' ')
    for x in range (int(coordinate_split[0]), int(coordinate_split[2])):
        for y in range(m-int(coordinate_split[3]), m-int(coordinate_split[1])):
            grid[y][x]=-1

for i in range (m):
    for j in range (n):
        if grid[i][j]==0:
            cnt+=1
            dfs(i, j)

print(cnt)

area.sort()
for num in area:
    print(num,end=" ") 