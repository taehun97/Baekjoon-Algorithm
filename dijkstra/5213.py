import sys
import heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
board = [['-' for _ in range(2*N)] for _ in range(N)]
for i in range(N):
    if i%2==0:
        for j in range(N):
            A, B = map(int, input().split())
            board[i][2*j] = A
            board[i][2*j+1] = B
    else:
        for j in range(N-1):
            A, B = map(int, input().split())
            board[i][2*j+1] = A
            board[i][2*j+2] = B
            
def dijkstra(start_x, start_y):
    distance = [[float('inf') for _ in range(2*N)] for _ in range(N)]
    distance [start_x][start_y] = 0
    
    max_block_num = -float('inf')
    final_route = []
    
    queue = []
    heapq.heappush(queue, (0, start_x, start_y, [1]))
    
    while queue:
        # print(queue)
        dist, cur_x, cur_y, route = heapq.heappop(queue)
        cur_block_num = getBlockNumber(cur_x, cur_y)
        
        if cur_block_num==N*N-N//2:
            return route
        
        if distance[cur_x][cur_y]<dist: continue
        
        if max_block_num<cur_block_num:
            max_block_num = cur_block_num
            final_route = route
        
        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            new_block_num = getBlockNumber(new_x, new_y)

            if 0<=new_x<N and 0<=new_y<2*N and (cur_block_num==new_block_num or board[cur_x][cur_y]==board[new_x][new_y]):
                if cur_block_num==new_block_num: new_distance = dist
                else: new_distance = dist + 1
                
                if distance[new_x][new_y]>new_distance:
                    distance[new_x][new_y] = new_distance
                    if cur_block_num==new_block_num:
                        heapq.heappush(queue, (new_distance, new_x, new_y, route))
                    else:
                        heapq.heappush(queue, (new_distance, new_x, new_y, route + [new_block_num]))
    return final_route
    
def getBlockNumber(x, y):
    if x%2==0: cur_block_num = (2 * N - 1) * (x // 2) + (y // 2) + 1
    else: cur_block_num = (2 * N - 1) * (x // 2) + ((y - 1) // 2) + N + 1
    
    return cur_block_num
    
r = dijkstra(0, 0)
print(len(r))
for e in r:
    print(e, end = ' ')
