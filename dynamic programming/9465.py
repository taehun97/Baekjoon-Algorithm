import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    board = []
    for i in range(2):
        board.append(list(map(int, input().split())))
        
    for i in range(1, n):
        if i==1:
            board[0][i] += board[1][i-1]
            board[1][i] += board[0][i-1] 
        else:
            board[0][i] += max(board[1][i-1], board[1][i-2])
            board[1][i] += max(board[0][i-1], board[0][i-2])

    print(max(board[0][n-1], board[1][n-1]))