import sys
import heapq

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

test_case = 1
while True:
    N = int(input())
    
    if N==0: break
    
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    
    visited[0][0] = board[0][0]
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0))
    answer = 0
    
    while queue:
        cost, cx, cy = heapq.heappop(queue)
        
        if cx==N-1 and cy==N-1:
            answer = cost
            break
        
        if visited[cx][cy]<cost: continue
        
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]>visited[cx][cy]+board[nx][ny]:
                    visited[nx][ny] = cost + board[nx][ny]
                    heapq.heappush(queue, (cost + board[nx][ny], nx, ny))

                
    print("Problem " + str(test_case) + ": " + str(answer))
    test_case += 1