import sys
import heapq

input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for _ in range(N):
    start, end, length = map(int, input().split())
    if end>D: continue
    graph[start].append((end, length))
    
for i in range(D):
    graph[i].append((i+1, 1))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(10001)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if cur_node>D: continue
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance

distances = dijkstra(0)
print(distances[D])