N, M = map(int, input().split())
board = [[0 for _ in range(M+1)] for _ in range(N+1)]
construction = [[False for _ in range((M+1)*2)] for _ in range((N+1)*2)]

K = int(input())
for _ in range(K):
    a, b, c, d = map(int, input().split())
    construction[a+c][b+d] = True

board[0][0] = 1    
for i in range(1, N+1):
    if construction[2*i-1][0]: break
    board[i][0] = 1
    
for i in range(1, M+1):
    if construction[0][2*i-1]: break
    board[0][i] = 1

for i in range(1, N+1):    
    for j in range(1, M+1):
        if not construction[2*i-1][2*j]:
            board[i][j] += board[i-1][j]
        if not construction[2*i][2*j-1]:
            board[i][j] += board[i][j-1]
  
print(board[N][M])