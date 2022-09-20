# 내 코드 어디가 틀린지 모르겠음;; 나만 차별해ㅡ.ㅡ
# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# state = [[[] for _ in range(N)] for _ in range(N)]
# info = []

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# # print(list(k[1] for k in temp))

# for i in range(K):
#     x, y, direction = map(int, input().split())
#     state[x-1][y-1].append([i, direction-1])
    
# # def getTokenIndex(x, y, num):
# #     for idx in range(len(state[x][y])):
# #         if num==state[x][y][0]:
# #             return idx
# #     return -1

# def whiteAction(cx, cy, nx, ny, idx):
#     # moving_token_list = state[cx][cy][idx:]
#     for i in range(idx, len(state[cx][cy])):
#         state[nx][ny].append(state[cx][cy][i])
#     del state[cx][cy][idx:]
        
# def redAction(cx, cy, nx, ny, idx):
#     # moving_token_list = state[cx][cy][idx:]
#     for i in range(len(state[cx][cy])-1, idx-1, -1):
#         state[nx][ny].append(state[cx][cy][i])
#     del state[cx][cy][idx:]    

# def changeDirection(x, y, i):
#     cd = state[x][y][i][1]
#     if cd==0: state[x][y][i][1] = 1
#     elif cd==1: state[x][y][i][1] = 0
#     elif cd==2: state[x][y][i][1] = 3
#     elif cd==3: state[x][y][i][1] = 2
    
#     return dx[state[x][y][i][1]], dy[state[x][y][i][1]]

# def isOverFourStack(i, j):
#     if len(state[i][j])>=4:
#         return True
#     return False

# # isGameOver = False
# round = 0 
# while True:
#     # for row in state:
#     #     print(*row)
#     round += 1
    
#     for k in range(K):
#         cx, cy = -1, -1
#         idx = -1
#         flag = False
        
#         for i in range(N):
#             for j in range(N):
#                 num_list = list(p[0] for p in state[i][j])
#                 if k in num_list:
#                     idx = num_list.index(k)
#                     cx, cy = i, j
#                     flag = True
#                     break
#             if flag: break
        
#         d = state[cx][cy][idx][1]
#         nx, ny = cx + dx[d], cy + dy[d]
        
#         if 0<=nx<N and 0<=ny<N: # moving grid is white
#             if board[nx][ny]==0:
#                 whiteAction(cx, cy, nx, ny, idx)
#                 if isOverFourStack(nx, ny):
#                     print(round)
#                     exit()
#             elif board[nx][ny]==1: # moving grid is red
#                 redAction(cx, cy, nx, ny, idx)
#                 if isOverFourStack(nx, ny):
#                     print(round)
#                     exit()
#         else:
#             ndx, ndy = changeDirection(cx, cy, idx)
#             nx, ny = cx + ndx, cy + ndy
#             if 0<=nx<N and 0<=ny<N:
#                 if board[nx][ny]==0:
#                     whiteAction(cx, cy, nx, ny, idx)
#                     if isOverFourStack(nx, ny):
#                         print(round)
#                         exit()
#                 elif board[nx][ny]==1: # moving grid is red
#                     redAction(cx, cy, nx, ny, idx)
#                     if isOverFourStack(nx, ny):
#                         print(round)
#                         exit()
        
#         # for row in state:
#         #     print(*row)
        
#         if round>1000:
#             print(-1)
#             exit()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(now_num):
    global horse

    now_x, now_y, now_d = horse[now_num]

    nx, ny, nd = now_x + dx[now_d], now_y + dy[now_d], now_d
    if nx < 0 or nx >= N or ny < 0 or ny >= N or chess_map[nx][ny] == 2:
        if 0 <= nd <= 1:
            nd = (nd + 1) % 2
        else:
            nd = (nd - 1) % 2 + 2
        nx, ny = now_x + dx[nd], now_y + dy[nd]
        horse[now_num][2] = nd

        if not (0 <= nx < N) or not (0 <= ny < N) or chess_map[nx][ny] == 2:
            return False

    if chess_map[nx][ny] == 0:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]

        chess_map_horse[nx][ny] += new_arr

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    elif chess_map[nx][ny] == 1:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]
        chess_map_horse[nx][ny] += new_arr[::-1]

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    return check_end()


def check_end():
    for i in range(N):
        for j in range(N):
            if len(chess_map_horse[i][j]) >= 4:
                return True
    return False


N, K = map(int, input().split())

chess_map = [list(map(int, input().split())) for _ in range(N)]
chess_map_horse = [[[] for _ in range(N)] for _ in range(N)]
horse = []
for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d - 1])
    chess_map_horse[x - 1][y - 1].append(i)

time = 0
flag = False
while True:

    if time > 1000:
        time = -1
        break
    if flag is True:
        break
    time += 1
    for i in range(K):
        if move(i):
            flag = True
            break

print(time)