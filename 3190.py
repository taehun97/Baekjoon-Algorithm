from collections import deque

# apple = 2 / blank = 0 / snake = 1
grid_row=int(input())
grid_col=grid_row
direction_change=[]
second=0;
direction_cnt=0;
snake_direction_x=0
snake_direction_y=1
snake_location=deque()
snake_location.append((0, 0))

grid=[[0]*grid_row for i in range (grid_col)]
grid[0][0]=1

apple_num=int(input())
for i in range (apple_num):
    apple_coordinate_str=input()
    grid[int(apple_coordinate_str.split()[0])-1][int(apple_coordinate_str.split()[1])-1]=2

direction_change_num=int(input())
for i in range (direction_change_num):
    direction_change_str=input()
    direction_change_x=direction_change_str.split()[0]
    direction_change_y=direction_change_str.split()[1]
    direction_change.append((direction_change_x, direction_change_y))

while (1):
    if direction_cnt<direction_change_num and second==int(direction_change[direction_cnt][0]):
        if direction_change[direction_cnt][1]=='D':
            if snake_direction_x==0 and snake_direction_y==1:
                snake_direction_x=1
                snake_direction_y=0
            elif snake_direction_x==0 and snake_direction_y==-1:
                snake_direction_x=-1
                snake_direction_y=0
            elif snake_direction_x==1 and snake_direction_y==0:
                snake_direction_x=0
                snake_direction_y=-1
            else:
                snake_direction_x=0
                snake_direction_y=1
        else:
            if snake_direction_x==0 and snake_direction_y==1:
                snake_direction_x=-1
                snake_direction_y=0
            elif snake_direction_x==0 and snake_direction_y==-1:
                snake_direction_x=1
                snake_direction_y=0
            elif snake_direction_x==1 and snake_direction_y==0:
                snake_direction_x=0
                snake_direction_y=1
            else:
                snake_direction_x=0
                snake_direction_y=-1
        direction_cnt+=1

    head_x, head_y=snake_location.popleft()
    temp_head_x=head_x
    temp_head_y=head_y
    head_x+=snake_direction_x
    head_y+=snake_direction_y

    if 0<=head_x<grid_row and 0<=head_y<grid_col and grid[head_x][head_y]!=1:
        snake_location.appendleft((temp_head_x, temp_head_y))
        snake_location.appendleft((head_x, head_y))
        
        if(grid[head_x][head_y]!=2):
            tail_x, tail_y=snake_location.pop()
            grid[tail_x][tail_y]=0

        grid[head_x][head_y]=1
        second+=1
    else:
        break

print(second+1)
