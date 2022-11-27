import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(n+1)]
    path = [[] for _ in range(n+1)]
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
                path[next_node] = path[cur_node] + [next_node]
                heapq.heappush(queue, (new_distance, next_node))
    
    result = [path[i][0] if i!=start else '-' for i in range(1, n+1)]     
    return result

answer = []
for i in range(1, n+1):
    answer.append(dijkstra(i))
    
for row in answer:
    print(*row)