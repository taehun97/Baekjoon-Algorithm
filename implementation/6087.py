import sys
from collections import deque

input = sys.stdin.readline

W, H = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[float('inf') for _ in range(W)] for _ in range(H)]
board = []
spots = []
candidates = []
for i in range(H):
    row = list(input().rstrip())
    board.append(row)
    
    for j in range(W):
        if row[j]=='C':
            spots.append((i, j))
            
start_x, start_y = spots[0]
end_x, end_y = spots[1]

def bfs(start_x, start_y):
    visited[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))
            
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for d in range(4):
            new_x, new_y = cur_x + dx[d], cur_y + dy[d]
            
            while True:
                # board의 범위를 벗어날 때
                if not (0<=new_x<H and 0<=new_y<W): break
                
                # 벽에 부딛혔을 때
                if board[new_x][new_y]=='*': break
                
                # 이전 방문보다 거울을 더 사용할 때
                if visited[new_x][new_y]<visited[cur_x][cur_y]+1: break
                
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[cur_x][cur_y] + 1
                new_x, new_y = new_x + dx[d], new_y + dy[d]

bfs(start_x, start_y)

print(visited[end_x][end_y] - 1)