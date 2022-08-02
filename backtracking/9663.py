import sys

input = sys.stdin.readline

n = int(input())

board = [-1 for _ in range(n)]
col_visited = [False for _ in range(n)]
case = 0

def findDeadlock(depth):
    global case
    
    if depth==n:
        case += 1
        return
    
    for i in range(n):
        if col_visited[i]: continue
        
        board[depth] = i
        if canLocated(depth):
            col_visited[i] = True
            findDeadlock(depth + 1)
            col_visited[i] = False

def canLocated(x):
    for i in range(x):
        if board[i]==board[x] or x-i==abs(board[x]-board[i]):
            return False
    
    return True
            
        

findDeadlock(0)
print(case)