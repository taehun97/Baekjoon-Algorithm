import sys

input = sys.stdin.readline

# 0: left 1: down 2: right 3: up
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

spread_percentage = [
    [(-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), (-1, 1, 1), (1, 1, 1), (-1, -1, 10), (1, -1, 10), (0, -2, 5)], 
    [(0, -1, 7), (0, 1, 7), (0, -2, 2), (0, 2, 2), (1, 1, 10), (1, -1, 10), (-1, -1, 1), (-1, 1, 1), (2, 0, 5)], 
    [(-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2), (-1, 1, 10), (1, 1, 10), (-1, -1, 1), (1, -1, 1), (0, 2, 5)], 
    [(0, -1, 7), (0, 1, 7), (0, -2, 2), (0, 2, 2), (-1, 1, 10), (-1, -1, 10), (1, -1, 1), (1, 1, 1), (-2, 0, 5)]
]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
center_x, center_y = N//2, N//2
answer = 0

for i in range(2*N-1):
    iteration_cnt = 0
    if i==2*N-2: iteration_cnt = i // 2
    else: iteration_cnt = i // 2 + 1
    
    for p in range(iteration_cnt):
        next_x, next_y = center_x + dx[i % 4], center_y + dy[i % 4]
        
        moved_sand = 0
        for mx, my, p in spread_percentage[i % 4]:
            if 0<=next_x + mx<N and 0<=next_y + my<N:
                board[next_x + mx][next_y + my] += board[next_x][next_y] * p // 100
            else: answer += board[next_x][next_y] * p // 100
                
            moved_sand += board[next_x][next_y] * p // 100
        
        if 0<=next_x + dx[i % 4]<N and 0<=next_y + dy[i % 4]<N:   
            board[next_x + dx[i % 4]][next_y + dy[i % 4]] += board[next_x][next_y] - moved_sand
        else: answer += board[next_x][next_y] - moved_sand
        board[next_x][next_y] = 0
        
        center_x, center_y = next_x, next_y
        
        # for row in board:
        #     print(*row)
        # print()
        
print(answer)