import sys

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
# 무게, 이동 칸수, 방향, 이동 완료 여부
board = [[[] for _ in range(N)] for _ in range(N)] 
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    board[r-1][c-1].append([m, s, d])
    
for _ in range(K):
    # 파이어볼의 다음 위치를 임시 board에 표시함
    temp_board = [[[] for _ in range(N)] for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                m, s, d = board[i][j][k]
                new_x, new_y = (i + s * dx[d]) % N, (j + s * dy[d]) % N
                
                temp_board[new_x][new_y].append([m, s, d])
    
    # 파이어볼 처리과정을 거친 후 결과를 board에 반영한다
    board = [[[] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if len(temp_board[i][j])==0: continue
            elif len(temp_board[i][j])==1:
                board[i][j].append(temp_board[i][j][0])
            else:
                new_m = 0
                new_s = 0
                new_d = 0
                
                isOdd = False
                isEven = False
                flag = False
                for k in range(len(temp_board[i][j])):
                    new_m += temp_board[i][j][k][0]
                    new_s += temp_board[i][j][k][1]
                    
                    if k==0:
                        if temp_board[i][j][k][2]%2==0:
                            isEven = True
                        else: isOdd = True
                    else:
                        if isEven:
                            if temp_board[i][j][k][2]%2==1:
                                flag = True
                        elif isOdd:
                            if temp_board[i][j][k][2]%2==0:
                                flag = True
                    
                new_m = new_m // 5
                new_s = new_s // len(temp_board[i][j])
                
                if new_m==0: continue
                
                for c in range(4):
                    if flag: board[i][j].append([new_m, new_s, 2 * c + 1])
                    else: board[i][j].append([new_m, new_s, 2 * c])
        
answer = 0        
for i in range(N):
    for j in range(N):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]
print(answer)              