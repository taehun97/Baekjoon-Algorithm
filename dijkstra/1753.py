import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
heap = []
distances = [float('inf') for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(s):
    global distances
    
    distances[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        current_distance, current_destination = heapq.heappop(heap)
        
        if distances[current_destination]<current_distance: continue
        
        for next_distance, next_destination in graph[current_destination]:
            d = next_distance + current_distance
            if d<distances[next_destination]:
                distances[next_destination] = d
                heapq.heappush(heap, (d, next_destination))

dijkstra(start)

for i in range(1, len(distances)):
    if distances[i]==float('inf'):
        print("INF")
    else: print(distances[i])