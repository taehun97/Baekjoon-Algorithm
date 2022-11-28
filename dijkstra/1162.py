import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
distance = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
    
# 1 -> N
def dijkstra(start):
    cnt = 0
    distance[start][cnt] = 0
    
    queue = []
    heapq.heappush(queue, (0, start, cnt))
    
    while queue:
        dist, cur_node, cur_cnt = heapq.heappop(queue)
            
        if distance[cur_node][cur_cnt]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node][cur_cnt]>new_distance:
                distance[next_node][cur_cnt] = new_distance
                heapq.heappush(queue, (new_distance, next_node, cur_cnt))
                
            if cur_cnt<K and distance[next_node][cur_cnt+1]>dist:
                distance[next_node][cur_cnt+1] = dist
                heapq.heappush(queue, (dist, next_node, cur_cnt + 1))

dijkstra(1)
print(min(distance[N]))
    