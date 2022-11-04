import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    start, end, time = map(int, input().split())    
    graph[start-1].append((end-1, time))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node]<dist: continue
        
        for next_node, d in graph[node]:
            new_distance = distance[node] + d
            if new_distance<distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance
        
round_trip = dijkstra(X-1)
for i in range(N):
    go = []
    if i!=X-1:
        go = dijkstra(i)
        round_trip[i] += go[X-1]
    
print(max(round_trip))
