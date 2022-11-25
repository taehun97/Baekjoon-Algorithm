import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    
def dijkstra():
    distance[1] = 0
    queue = []
    heapq.heappush(queue, (0, 1))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                parent[next_node] = cur_node
                heapq.heappush(queue, (new_distance, next_node))
                
dijkstra()

print(N-1)
for i in range(2, N+1):
    print(i, parent[i])