import sys

def divAndCon(arr, start_x, start_y, end_x, end_y): # 0, 0, 7, 7 -> (0, 0), (7, 7)
    global white_grid, blue_grid
    standard_grid_color=arr[start_x][start_y]
    for i in range (start_x, end_x+1):
        for j in range (start_y, end_y+1):
            if standard_grid_color!=arr[i][j]:
                divAndCon(arr, start_x, start_y, (start_x+end_x)//2, (start_y+end_y)//2) # 0, 0, 3, 3 -> (0, 0), (3, 3) | section 1
                divAndCon(arr, start_x, (start_y+end_y)//2+1, (start_x+end_x)//2, end_y) # 0, 4, 4, 7 -> (0, 4), (3, 7) | section 2
                divAndCon(arr, (start_x+end_x)//2+1, start_y, end_x, (start_y+end_y)//2) # 4, 0, 7, 3 -> (4, 0), (7, 3) | section 3
                divAndCon(arr, (start_x+end_x)//2+1, (start_y+end_y)//2+1, end_x, end_y) # 4, 4, 7, 7 -> (4, 4), (7, 7) | section 4
                return 
    if standard_grid_color==0: white_grid+=1
    else: blue_grid+=1        

r=sys.stdin.readline
N=int(r())
square=[]
white_grid=0
blue_grid=0

for i in range (N):
    square.append(list(map(int, r().split())))
    
divAndCon(square, 0, 0, N-1, N-1)

print(white_grid)
print(blue_grid)