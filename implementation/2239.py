import sys

input = sys.stdin.readline
board = []
q = []

for i in range(9):
    row = list(map(int, list(input().rstrip())))
    board.append(row)
    
    for j in range(0, 9):
        if row[j]==0: q.append((i, j))

def backtracking(n):
    if n==len(q):
        for row in board:
            print(*row, sep='')
        sys.exit(0)
    
    candidates = [c for c in range(1, 10)]
    x, y = q[n]
    
    bx = x//3
    by = y//3
    
    for e in range(0, 9):
        if board[x][e] in candidates: candidates.remove(board[x][e])
        
    for e in range(0, 9):
        if board[e][y] in candidates: candidates.remove(board[e][y])
        
    for ex in range(bx*3, bx*3+3):
        for ey in range(by*3, by*3+3):
            if board[ex][ey] in candidates: candidates.remove(board[ex][ey])
            
    for c in candidates:
        board[x][y] = c
        backtracking(n+1)
    board[x][y] = 0

backtracking(0)