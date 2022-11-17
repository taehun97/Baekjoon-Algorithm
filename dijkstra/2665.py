import sys
import heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

def dijkstra(start_x, start_y):
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]
    distance[start_x][start_y] = 0
    
    queue = []
    heapq.heappush(queue, (0, start_x, start_y))
    
    while queue:
        count, cx, cy = heapq.heappop(queue)
        
        if distance[cx][cy]<count: continue
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==0: new_distance = count + 1
                else: new_distance = count
                
                if distance[nx][ny]>new_distance:
                    distance[nx][ny] = new_distance
                    heapq.heappush(queue, (new_distance, nx, ny))
    
    return distance[n-1][n-1]

print(dijkstra(0, 0))