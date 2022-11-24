import sys
import heapq
from collections import deque

input = sys.stdin.readline

def dijkstra():
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        # if distance[cur_node]<dist: continue
        if cur_node==end: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if not visited[cur_node][next_node] and distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
    
def bfs():
    queue = deque()
    queue.append(end)
    
    while queue:
        cur_node = queue.popleft()

        if cur_node==start: continue
        
        for prev_node, prev_dist in rev_graph[cur_node]:
            if not visited[prev_node][cur_node] and prev_dist+distance[prev_node]==distance[cur_node]:
                visited[prev_node][cur_node] = True
                queue.append(prev_node)

while True:
    N, M = map(int, input().split())
    if N<2: break
    
    start, end = map(int, input().split())
    
    distance = [float('inf') for _ in range(N)]
    
    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append([V, P])
        rev_graph[V].append([U, P])

    visited = [[False for _ in range(N)] for _ in range(N)]

    dijkstra()
    bfs()
    
    distance = [float('inf') for _ in range(N)]
    dijkstra()
    bfs()
    
    if distance[end]==float('inf'): print(-1)
    else: print(distance[end])