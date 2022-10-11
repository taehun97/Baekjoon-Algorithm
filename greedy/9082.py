import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    board = []
    board.append(list(map(int, list(input().rstrip()))))
    board.append(list(input().rstrip()))
    
    board_sum = sum(board[0])
    
    if board[0][0]==0 and board[0][-1]==0:
        print(board_sum // 3)
    elif (board[0][0]==0 and board[0][-1]!=0) or (board[0][0]!=0 and board[0][-1]==0):
        print((board_sum + 1) // 3)
    else:
        print((board_sum + 2) // 3)        