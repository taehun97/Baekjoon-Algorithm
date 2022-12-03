import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(sx, sy):
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    visited[sx][sy] = 0
    
    queue = deque()
    queue.append((sx, sy))
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if 0<=new_x<=h+1 and 0<=new_y<=w+1:
                if visited[new_x][new_y]==-1:
                    if board[new_x][new_y]=='.' or board[new_x][new_y]=='$':
                        visited[new_x][new_y] = visited[cur_x][cur_y]
                        queue.appendleft((new_x, new_y))
                    elif board[new_x][new_y]=='#':
                        visited[new_x][new_y] = visited[cur_x][cur_y] + 1
                        queue.append((new_x, new_y))
    return visited

test_case = int(input())
for _ in range(test_case):
    h, w = map(int, input().split())
    board = []
    locations = []
    board.append(['.']*(w+2))
    for i in range(1, h+1):
        row = list('.' + input().rstrip() + '.')
        board.append(row)
        
        for j in range(w+2):
            if row[j]=='$':
                locations.append((i, j))
    board.append(['.']*(w+2))
                
    first = dijkstra(locations[0][0], locations[0][1])
    second = dijkstra(locations[1][0], locations[1][1])
    third = dijkstra(0, 0)
    
    ans = float('inf')
    for i in range(1, h+1):
        for j in range(1, w+1):
            if first[i][j]!=-1 and second[i][j]!=-1 and third[i][j]!=-1:
                local_ans = first[i][j] + second[i][j] + third[i][j]
                if board[i][j]=='#': local_ans -= 2
                ans = min(ans, local_ans)
    print(ans)