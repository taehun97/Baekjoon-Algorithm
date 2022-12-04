import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
visible = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    
    if a!=N-1 and visible[a]==1: continue
    if b!=N-1 and visible[b]==1: continue
    
    graph[a].append((b, t))
    graph[b].append((a, t))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = dist + next_dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    if distance[N-1]==float('inf'): return -1
    else: return distance[N-1]
    
print(dijkstra(0))