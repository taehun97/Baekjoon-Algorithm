import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start, max_cnt):
    distance = [[float('inf') for _ in range(k)] for _ in range(n+1)]
    distance[start][0] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node][max_cnt-1]>new_distance:
                distance[next_node][max_cnt-1] = new_distance
                distance[next_node].sort()
                heapq.heappush(queue, (new_distance, next_node))
    return distance

d = dijkstra(1, k)

for i in range(1, n+1):
    if d[i][k-1]==float('inf'): print(-1)
    else: print(d[i][k-1])