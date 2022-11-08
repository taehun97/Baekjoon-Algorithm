import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))
    
def bfs(id, x, y):
    global answer, visited
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    answer[x][y] = id
    
    count = 1
    while queue:
        cx, cy = queue.popleft()
        
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny]==0:
                visited[nx][ny] = True
                answer[nx][ny] = id
                queue.append((nx, ny))
                count += 1
    
    return count
                
    
visited = [[False for _ in range(M)] for _ in range(N)]
answer = [[0 for _ in range(M)] for _ in range(N)]
dictionary = {}
identifier = 1
for i in range(N):
    for j in range(M):
        if board[i][j]==1 or visited[i][j]: continue
        cnt = bfs(identifier, i, j)
        dictionary[identifier] = cnt
        identifier += 1

result = [[1 for _ in range(M)] for _ in range(N)]        
for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            result[i][j] = 0
            continue
        
        neighbors = set()
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
                neighbors.add(answer[nx][ny])
                
        for idf in neighbors:
            result[i][j] += dictionary[idf]
            result[i][j] %= 10
            
for i in range(N):
    for j in range(M):
        print(result[i][j], end = '')
    print()