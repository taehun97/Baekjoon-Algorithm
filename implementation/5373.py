import sys

input = sys.stdin.readline

T = int(input())

def rotate90CounterClockwise(a):
    result = [[0]*3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            result[r][c] = a[c][2-r]   
    return result

def rotate90Clockwise(a):
    result = [[0]*3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            result[r][c] = a[2-c][r]
    return result

for _ in range(T):
    n = int(input())
    rotates = input().split()
    cube = [["*"]*9 for _ in range(12)]
    
    for i in range(12):
        if i//3==0:
            cube[i] = ["*", "*", "*", "o", "o", "o", "*", "*", "*"]
        elif i//3==1:
            cube[i] = ["*", "*", "*", "w", "w", "w", "*", "*", "*"]
        elif i//3==2:
            cube[i] = ["g", "g", "g", "r", "r", "r", "b", "b", "b"]
        else:
            cube[i] = ["*", "*", "*", "y", "y", "y", "*", "*", "*"]
    
    for rotate in rotates:
        rotate_plane = rotate[0]
        rotate_direction = rotate[1]
        

        
        if rotate_plane=='U':
            temp = [cube[i][3:6] for i in range(12) if i//3==1]
            rotate_temp = []
            
            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)
                for i in range(3):
                    cube[6][6+i], cube[2][5-i], cube[6][i], cube[6][3+i] = cube[6][3+i], cube[6][6+i], cube[2][5-i], cube[6][i]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[6][3+i], cube[6][6+i], cube[2][5-i], cube[6][i] = cube[6][6+i], cube[2][5-i], cube[6][i], cube[6][3+i]
                    
            for i in range(3):
                for j in range(3):
                    cube[i+3][j+3] = rotate_temp[i][j]
            
        elif rotate_plane=='D':
            temp = [cube[i][3:6] for i in range(12) if i//3==3]
            rotate_temp = []
            
            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)
                for i in range(3):
                    cube[8][3+i], cube[8][6+i], cube[0][5-i], cube[8][i] = cube[8][6+i], cube[0][5-i], cube[8][i], cube[8][3+i]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[8][6+i], cube[0][5-i], cube[8][i], cube[8][3+i] = cube[8][3+i], cube[8][6+i], cube[0][5-i], cube[8][i]
                    
            for i in range(3):
                for j in range(3):
                    cube[i+9][j+3] = rotate_temp[i][j]
                    
        elif rotate_plane=='F':
            temp = [cube[i][3:6] for i in range(12) if i//3==2]
            rotate_temp = []
            
            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)  
                for i in range(3):
                    cube[8-i][2], cube[9][5-i], cube[6+i][6], cube[5][3+i] = cube[5][3+i], cube[8-i][2], cube[9][5-i], cube[6+i][6]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[5][3+i], cube[8-i][2], cube[9][5-i], cube[6+i][6] = cube[8-i][2], cube[9][5-i], cube[6+i][6], cube[5][3+i]
                
            for i in range(3):
                for j in range(3):
                    cube[i+6][j+3] = rotate_temp[i][j]
                
        elif rotate_plane=='B':
            temp = [cube[i][3:6] for i in range(12) if i//3==0]
            rotate_temp = []         

            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)
                for i in range(3):
                    cube[3][3+i], cube[6+i][8], cube[11][5-i], cube[8-i][0] = cube[8-i][0], cube[3][3+i], cube[6+i][8], cube[11][5-i]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[8-i][0], cube[3][3+i], cube[6+i][8], cube[11][5-i] = cube[3][3+i], cube[6+i][8], cube[11][5-i], cube[8-i][0]
                    
            for i in range(3):
                for j in range(3):
                    cube[i][j+3] = rotate_temp[i][j]
                
        elif rotate_plane=='R':
            temp = [cube[i][6:9] for i in range(12) if i//3==2]
            rotate_temp = []
            
            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)
                for i in range(3):
                    cube[i][5], cube[3+i][5], cube[6+i][5], cube[9+i][5] = cube[9+i][5], cube[i][5], cube[3+i][5], cube[6+i][5]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[9+i][5], cube[i][5], cube[3+i][5], cube[6+i][5] = cube[i][5], cube[3+i][5], cube[6+i][5], cube[9+i][5]
                    
            for i in range(3):
                for j in range(3):
                    cube[i+6][j+6] = rotate_temp[i][j]
                
        elif rotate_plane=='L':
            temp = [cube[i][0:3] for i in range(12) if i//3==2]
            rotate_temp = []
            
            if rotate_direction=='-':
                rotate_temp = rotate90CounterClockwise(temp)
                for i in range(3):
                    cube[i][3], cube[i+3][3], cube[i+6][3], cube[i+9][3] = cube[i+3][3], cube[i+6][3], cube[i+9][3], cube[i][3]
            elif rotate_direction=='+':
                rotate_temp = rotate90Clockwise(temp)
                for i in range(3):
                    cube[i+3][3], cube[i+6][3], cube[i+9][3], cube[i][3] = cube[i][3], cube[i+3][3], cube[i+6][3], cube[i+9][3]
                    
            for i in range(3):
                for j in range(3):
                    cube[i+6][j] = rotate_temp[i][j]
                    
    for i in range(3):
        for j in range(3):
            print(cube[i+3][j+3], end='')
        print()
    
