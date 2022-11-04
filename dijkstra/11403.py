import sys
import heapq

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# Dijkstra Solution
# def dijkstra(start, n):
#     distance[start][start] = 0
#     queue = []
#     heapq.heappush(queue, (0, start))
    
#     while queue:
#         dist, node = heapq.heappop(queue)
        
#         if distance[start][node]<dist: continue
        
#         for next_node in range(n):
#             if graph[node][next_node]==0: continue    
            
#             new_distance = distance[start][node] + graph[node][next_node]
#             if new_distance<distance[start][next_node] or next_node==start:
#                 distance[start][next_node] = new_distance
#                 heapq.heappush(queue, (new_distance, next_node))
                
# distance = [[float('inf') for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     dijkstra(i, N)
    
# for i in range(N):
#     for j in range(N):
#         if distance[i][j]!=float('inf') and distance[i][j]!=0: print(1, end=' ')
#         else: print(0, end=' ')
#     print()
    
#Floid-Warshall Solution
def floidWarshall(g, n):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    # initialization
    for i in range(n):
        for j in range(n):
            if g[i][j]!=0: dist[i][j] = g[i][j]
            
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

distance = floidWarshall(graph, N)

for i in range(N):
    for j in range(N):
        if distance[i][j]!=float('inf') and distance[i][j]!=0: print(1, end=' ')
        else: print(0, end=' ')
    print()