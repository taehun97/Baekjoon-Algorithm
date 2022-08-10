import sys

input = sys.stdin.readline
board = []
candidates = []

isOver = False
def dfs(x):
    global isOver
    
    if isOver: return
    
    if x==len(candidates):
        isOver = True
        for row in board:
            print(*row)
        return
    
    else:
        p, q = candidates[x]
        
        promising = isPromising(p, q)
        for element in promising:
            board[p][q] = element
            dfs(x+1)
            board[p][q] = 0
            
def isPromising(x, y):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(9):
        if board[i][y] in num_list:
            num_list.remove(board[i][y])
        if board[x][i] in num_list:
            num_list.remove(board[x][i])
            
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if board[i][j] in num_list:
                num_list.remove(board[i][j])
                
    return num_list
            

for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(9):
        if row[j]==0:
            candidates.append((i, j))

dfs(0)