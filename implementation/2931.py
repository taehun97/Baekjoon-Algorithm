import sys

input = sys.stdin.readline

R, C = map(int, input().split())
directionDict = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)],
                 '+': [(-1, 0), (1, 0), (0, -1), (0, 1)],
                 '1': [(1, 0), (0, 1)], '2': [(-1, 0), (0, 1)], 
                 '3': [(-1, 0), (0, -1)], '4': [(1, 0), (0, -1)]}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start_x, start_y, end_x, end_y = -1, -1, -1, -1
board = []
for i in range(R):
    row = list(input().rstrip())
    board.append(row)
    
    for j in range(C):
        if row[j]=="M": start_x, start_y = i, j
        elif row[j]=="Z": end_x, end_y = i, j

# find missing point        
def findMissingPoint():
    for i in range(R):
        for j in range(C):
            if board[i][j]=='.' or board[i][j]=='M' or board[i][j]=='Z': pass
            elif board[i][j]=='|':
                if not (board[i-1][j]=='|' or board[i-1][j]=='+' or board[i-1][j]=='1' or board[i-1][j]=='4' or board[i-1][j]=='M' or board[i-1][j]=='Z'):
                    return i - 1, j
                if not (board[i+1][j]=='|' or board[i+1][j]=='+' or board[i+1][j]=='2' or board[i+1][j]=='3' or board[i+1][j]=='M' or board[i+1][j]=='Z'):
                    return i + 1, j
            elif board[i][j]=='-':
                if not (board[i][j-1]=='-' or board[i][j-1]=='+' or board[i][j-1]=='1' or board[i][j-1]=='2' or board[i][j-1]=='M' or board[i][j-1]=='Z'):
                    return i, j - 1
                if not (board[i][j+1]=='-' or board[i][j+1]=='+' or board[i][j+1]=='3' or board[i][j+1]=='4' or board[i][j+1]=='M' or board[i][j+1]=='Z'):
                    return i, j + 1
            elif board[i][j]=='+':
                if not (board[i-1][j]=='|' or board[i-1][j]=='+' or board[i-1][j]=='1' or board[i-1][j]=='4' or board[i-1][j]=='M' or board[i-1][j]=='Z'):
                    return i - 1, j
                if not (board[i+1][j]=='|' or board[i+1][j]=='+' or board[i+1][j]=='2' or board[i+1][j]=='3' or board[i+1][j]=='M' or board[i+1][j]=='Z'):
                    return i + 1, j
                if not (board[i][j-1]=='-' or board[i][j-1]=='+' or board[i][j-1]=='1' or board[i][j-1]=='2' or board[i][j-1]=='M' or board[i][j-1]=='Z'):
                    return i, j - 1
                if not (board[i][j+1]=='-' or board[i][j+1]=='+' or board[i][j+1]=='3' or board[i][j+1]=='4' or board[i][j+1]=='M' or board[i][j+1]=='Z'):
                    return i, j + 1
            elif board[i][j]=='1':
                if not (board[i][j+1]=='-' or board[i][j+1]=='+' or board[i][j+1]=='3' or board[i][j+1]=='4' or board[i][j+1]=='M' or board[i][j+1]=='Z'):
                    return i, j + 1
                if not (board[i+1][j]=='|' or board[i+1][j]=='+' or board[i+1][j]=='2' or board[i+1][j]=='3' or board[i+1][j]=='M' or board[i+1][j]=='Z'):
                    return i + 1, j
            elif board[i][j]=='2':
                if not (board[i-1][j]=='|' or board[i-1][j]=='+' or board[i-1][j]=='1' or board[i-1][j]=='4' or board[i-1][j]=='M' or board[i-1][j]=='Z'):
                    return i - 1, j
                if not (board[i][j+1]=='-' or board[i][j+1]=='+' or board[i][j+1]=='3' or board[i][j+1]=='4' or board[i][j+1]=='M' or board[i][j+1]=='Z'):
                    return i, j + 1
            elif board[i][j]=='3':
                if not (board[i-1][j]=='|' or board[i-1][j]=='+' or board[i-1][j]=='1' or board[i-1][j]=='4' or board[i-1][j]=='M' or board[i-1][j]=='Z'):
                    return i - 1, j
                if not (board[i][j-1]=='-' or board[i][j-1]=='+' or board[i][j-1]=='1' or board[i][j-1]=='2' or board[i][j-1]=='M' or board[i][j-1]=='Z'):
                    return i, j - 1
            elif board[i][j]=='4':
                if not (board[i][j-1]=='-' or board[i][j-1]=='+' or board[i][j-1]=='1' or board[i][j-1]=='2' or board[i][j-1]=='M' or board[i][j-1]=='Z'):
                    return i, j - 1
                if not (board[i+1][j]=='|' or board[i+1][j]=='+' or board[i+1][j]=='2' or board[i+1][j]=='3' or board[i+1][j]=='M' or board[i+1][j]=='Z'):
                    return i + 1, j
    return -1, -1

def findAppropriatePipe(x, y):
    up = isUpperConnectable(x, y)
    down = isLowerConnectable(x, y)
    left = isLeftConnectable(x, y)
    right = isRightConnectable(x, y)
    
    if up and down and left and right: return '+'
    elif up and down and not left and not right: return '|'
    elif not up and not down and left and right: return '-'
    elif not up and down and not left and right: return '1'
    elif up and not down and not left and right: return '2'
    elif up and not down and left and not right: return '3'
    elif not up and down and left and not right: return '4'
    else: return ''
    
def isUpperConnectable(i, j):
    if not (0<=i-1<R and 0<=j<C): return False
    if board[i-1][j]=='|' or board[i-1][j]=='+' or board[i-1][j]=='1' or board[i-1][j]=='4':
        return True
    else: return False
    
def isLowerConnectable(i, j):
    if not (0<=i+1<R and 0<=j<C): return False
    if board[i+1][j]=='|' or board[i+1][j]=='+' or board[i+1][j]=='2' or board[i+1][j]=='3':
        return True
    else: return False

def isLeftConnectable(i, j):
    if not (0<=i<R and 0<=j-1<C): return False
    if board[i][j-1]=='-' or board[i][j-1]=='+' or board[i][j-1]=='1' or board[i][j-1]=='2':
        return True
    else: return False
    
def isRightConnectable(i, j):
    if not (0<=i<R and 0<=j+1<C): return False
    if board[i][j+1]=='-' or board[i][j+1]=='+' or board[i][j+1]=='3' or board[i][j+1]=='4':
        return True
    else: return False

mpx, mpy = findMissingPoint()
pipe = findAppropriatePipe(mpx, mpy)

print(mpx + 1, mpy + 1, pipe)
