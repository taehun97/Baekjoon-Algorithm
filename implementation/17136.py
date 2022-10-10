from re import L
import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
answer = sys.maxsize
block_cnt = [5, 5, 5, 5, 5]

def isBlockPossible(x, y, n, b):
    for i in range(x, x+n+1):
        for j in range(y, y+n+1):
            if b[i][j]==0: return False
    return True

def visitBlock(x, y, n, b):
    for i in range(x, x+n+1):
        for j in range(y, y+n+1):
            b[i][j] = 0

def backtrackBlock(x, y, n, b):
    for i in range(x, x+n+1):
        for j in range(y, y+n+1):
            b[i][j] = 1

def dfs(x, y, cnt):
    # print(x, y, cnt)
    global answer
    global block_cnt

    if y>=10:
        answer = min(answer, cnt)
        return
    
    if x>=10:
        dfs(0, y+1, cnt)
        return

    if board[x][y]==1:
        for n in range(5):
            if block_cnt[n]==0: continue
            
            if x+n>=10 or y+n>=10: continue
            
            flag = isBlockPossible(x, y, n, board)
            
            if flag:
                visitBlock(x, y, n, board)
                block_cnt[n] -= 1
                
                dfs(x + n + 1, y, cnt + 1)

                backtrackBlock(x, y, n, board)
                block_cnt[n] += 1
    else:
        dfs(x + 1, y, cnt)
            
            
dfs(0, 0, 0)

if answer==sys.maxsize: print(-1)
else: print(answer)