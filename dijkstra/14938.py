import sys
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
cost = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(n+1)]
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
    
answer = 0
for i in range(1, n+1):
    d = dijkstra(i)
    print(d)
    print(answer)
    
    local_answer = 0
    for j in range(1, n+1):
        if d[j]<=m:
            print("ADD")
            print(d[i], m)
            local_answer += cost[j]
    
    answer = max(answer, local_answer)
    print(answer)
print(answer)