import sys
import heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split()) # col, row
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))
    
def solve():
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    
    while queue:
        count, cur_x, cur_y = heapq.heappop(queue)
        
        if cur_x==N-1 and cur_y==M-1:
            return count
        
        for d in range(4):
            new_x, new_y = cur_x + dx[d], cur_y + dy[d]
            if 0<=new_x<N and 0<=new_y<M and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if board[new_x][new_y]==1:
                    heapq.heappush(queue, (count + 1, new_x, new_y))
                else:
                    heapq.heappush(queue, (count, new_x, new_y))
    
print(solve())