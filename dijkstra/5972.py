import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    Ai, Bi, Ci = map(int, input().split())
    graph[Ai].append((Bi, Ci))
    graph[Bi].append((Ai, Ci))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance
    
distances = dijkstra(1)
print(distances[N])