import sys
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    
def dijkstra(start_node):
    distance = [float('inf') for _ in range(N+1)]
    distance[start_node] = 0
    
    queue = []
    heapq.heappush(queue, (0, start_node))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<dist: continue
        
        for next_node in graph[cur_node]:
            new_distance = dist + 1
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
    
    return distance
    
d = dijkstra(X)
answer = []
for i in range(len(d)):
    if d[i]==K: answer.append(i)

if len(answer)==0: print(-1)
else:
    for ans in answer:
        print(ans)