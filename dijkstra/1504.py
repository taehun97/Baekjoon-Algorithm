import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
    
p, q = map(int, input().split())
v1, v2 = p - 1, q - 1

def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = distance[cur_node] + next_dist
            
            if new_distance<distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance

distance = dijkstra(0)
distance2 = dijkstra(v1)
distance3 = dijkstra(v2)

route1 = distance[v1] + distance2[v2] + distance3[N-1]
route2 = distance[v2] + distance3[v1] + distance2[N-1]

if route1==float('inf') and route2==float('inf'): print(-1)
else: print(min(route1, route2))