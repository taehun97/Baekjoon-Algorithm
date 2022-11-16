import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
start_city, end_city = map(int, input().split())
    
def dijkstra(start):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    
    path = [[] for _ in range(n+1)]
    path[start].append(start)
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        print(queue)
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = dist + next_dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                path[next_node] = path[cur_node] + [next_node]
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance, path

d, p = dijkstra(start_city)
print(d[end_city])
print(len(p[end_city]))
for c in p[end_city]:
    print(c, end = ' ')