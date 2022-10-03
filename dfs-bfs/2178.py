import sys

r=sys.stdin.readline

N, M=map(int, r().split())
queue=[(0, 0)]
FOUR_DIRECTION=4
maze=[]
move_x=[1, 0, -1, 0]
move_y=[0, 1, 0, -1]
end_coordinate=(N-1, M-1)

# maze initialize
for _ in range (N):
    temp_list=list(r())
    maze.append([int(temp_list[i]) for i in range (len(temp_list)-1)])

def dfs_maze():
    while queue:
        x, y=queue.pop(0)
        if x==end_coordinate[0] and y==end_coordinate[1]:
            print(maze[x][y])
            return
        else:
            for i in range (FOUR_DIRECTION):
                new_x=x+move_x[i]
                new_y=y+move_y[i]
                if new_x>=0 and new_x<N and new_y>=0 and new_y<M:
                    if maze[new_x][new_y]==1:
                        maze[new_x][new_y]=maze[x][y]+1
                        queue.append((new_x, new_y))
    
dfs_maze()