import sys

input = sys.stdin.readline

N = int(input())
student_list = []
board = [[-1]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N**2):
    row = list(map(int, input().split()))
    student_list.append((row[0], (row[1], row[2], row[3], row[4])))
    
def adjacentStudents(x, y, s_num):
    result = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] in student_list[s_num][1]:
            result += 1
    return result

def adjacentBlank(x, y):
    result = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==-1:
            result += 1
    return result

def favorableStudents(x, y):
    result = 0
    for i in range(N**2):
        if board[x][y]==student_list[i][0]:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0<=nx<N and 0<=ny<N and board[nx][ny] in student_list[i][1]:
                    result += 1
            break
    return result

for s in range(N**2):
    # First Priority
    max_adjacent_students = 0
    adjacent_students = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j]!=-1: continue
                      
            local_adjacent_students_num = adjacentStudents(i, j, s)
            if local_adjacent_students_num==max_adjacent_students:
                adjacent_students.append((i, j))
            elif local_adjacent_students_num>max_adjacent_students:
                adjacent_students.clear()
                adjacent_students.append((i, j))
                max_adjacent_students = local_adjacent_students_num
                
    if len(adjacent_students)==1:
        board[adjacent_students[0][0]][adjacent_students[0][1]] = student_list[s][0]
        continue
    
    # Second Priority
    max_blank_num = 0
    max_blank_block_list = []
    
    for x, y in adjacent_students:
        local_blank = adjacentBlank(x, y)
        if local_blank==max_blank_num:
            max_blank_block_list.append((x, y))
        elif local_blank>max_blank_num:
            max_blank_block_list.clear()
            max_blank_block_list.append((x, y))
            max_blank_num = local_blank
            
    if len(max_blank_block_list)==1:
        board[max_blank_block_list[0][0]][max_blank_block_list[0][1]] = student_list[s][0]
        continue
    
    # Third Priority
    min_row = float('inf')
    min_row_list = []
    
    for x, y in max_blank_block_list:
        if min_row>x:
            min_row = x
            min_row_list.clear()
            min_row_list.append((x, y))
        elif min_row==x:
            min_row_list.append((x, y))
            
    if len(min_row_list):
        board[min_row_list[0][0]][min_row_list[0][1]] = student_list[s][0]
        continue
    
    min_col = float('inf')
    final_coord_x, final_coord_y = -1, -1    
    for x, y in min_row_list:
        if min_col>y:
            min_col = y
            final_coord_x, final_coord_y = x, y
        
    board[final_coord_x][final_coord_y] = student_list[s][0]
    

answer = 0    
for i in range(N):
    for j in range(N):
        f_students = favorableStudents(i, j)
        if f_students==1:
            answer += 1
        elif f_students==2:
            answer += 10
        elif f_students==3:
            answer += 100
        elif f_students==4:
            answer += 1000
            
print(answer)