import sys

r=sys.stdin.readline

row, col=tuple(map(int, r().split()))
chess_board=[]
board_row=8
board_col=8
wrong_color=0

for _ in range (row):
    chess_board.append(list(r()))
    
# 기준이 B일때
for c in range (2):
    if c==0: color=['B', 'W']
    else: color=['W', 'B']        
    for x_first in range(row-board_row+1):
        for y_first in range(col-board_col+1):
            temp_wrong_color=0
            for x in range (board_row):
                for y in range (board_col):
                    if (x+y)%2==0 and chess_board[x_first+x][y_first+y]==color[1]:
                        temp_wrong_color+=1
                    elif (x+y)%2==1 and chess_board[x_first+x][y_first+y]==color[0]:
                        temp_wrong_color+=1
            if (x_first==0 and y_first==0 and c==0) or wrong_color>temp_wrong_color:
                wrong_color=temp_wrong_color
            
print(wrong_color)