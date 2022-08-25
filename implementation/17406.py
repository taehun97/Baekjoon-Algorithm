import sys
from itertools import permutations
import copy

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
calculations = [tuple(map(int, input().split())) for _ in range(k)]
cases = list(permutations(calculations, k))

def rotation(cx, cy, radius):
    global temp_board
    
    for r in range(radius, 0, -1):
        upper_row = temp_board[cx-r][cy-r:cy+r]
        lower_row = temp_board[cx+r][cy-r+1:cy+r+1]
        left_col = list(temp_board[i][cy-r] for i in range(cx-r+1, cx+r+1))
        right_col = list(temp_board[i][cy+r] for i in range(cx-r, cx+r))

        
        for j in range(len(upper_row)):
            temp_board[cx-r][cy-r+j+1] = upper_row[j]
        for j in range(len(lower_row)):
            temp_board[cx+r][cy-r+j] = lower_row[j]
        for j in range(len(left_col)):
            temp_board[cx-r+j][cy-r] = left_col[j]
        for j in range(len(right_col)):
            temp_board[cx-r+1+j][cy+r] = right_col[j]
            
minimum = float('inf')
for i in range(len(cases)):
    temp_board = copy.deepcopy(board)
    for (r, c, s) in cases[i]:
        rotation(r-1, c-1, s)
    for j in range(len(board)):
        minimum = min(minimum, sum(temp_board[j]))
        
print(minimum)
