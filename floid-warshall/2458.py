import sys
import heapq

input = sys.stdin.readline

# Dijkstra Solution
# N, M = map(int, input().split())

# bigger_graph = [[] for _ in range(N+1)]
# smaller_graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split()) # a < b
#     bigger_graph[a].append(b)
#     smaller_graph[b].append(a)
    
# def dijkstra(start_node, graph):
#     distance = [float('inf') for _ in range(N+1)]
#     distance[start_node] = 0
    
#     queue = []
#     heapq.heappush(queue, (0, start_node))
    
#     while queue:
#         dist, cur_node = heapq.heappop(queue)
        
#         if distance[cur_node]<dist: continue
        
#         for next_node in graph[cur_node]:
#             new_distance = dist + 1
#             if distance[next_node]>new_distance:
#                 distance[next_node] = new_distance
#                 heapq.heappush(queue, (new_distance, next_node))
                
#     return distance

# answer = 0
# for i in range(1, N+1):
#     bd = dijkstra(i, bigger_graph)
#     sd = dijkstra(i, smaller_graph)
    
#     flag = False
#     for j in range(1, N+1):
#         if j==i: continue
        
#         if bd[j]==float('inf') and sd[j]==float('inf'):
#             flag = True
            
#     if not flag: answer += 1
    
# print(answer)

# Floid-Warshall Solution
N, M = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    tall, short = map(int, input().split())
    graph[tall][short] = 1
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j] = 1

ans = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        cnt += graph[i][j] + graph[j][i]
    if cnt==N-1: ans += 1
    
print(ans) 