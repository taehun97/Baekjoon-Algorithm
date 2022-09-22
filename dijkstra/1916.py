import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
    
distances = [float('inf') for _ in range(N+1)]

def dijkstra(s):
    heap = []
    distances[s] = 0
    heapq.heappush(heap, (s, 0))
    
    while heap:
        current_destination, current_distance = heapq.heappop(heap)
        
        if distances[current_destination]<current_distance:
            continue
        
        for next_destination, next_distance in graph[current_destination]:
            d = next_distance + current_distance
            if d<distances[next_destination]:
                distances[next_destination] = d
                heapq.heappush(heap, (next_destination, d))

start_city, end_city = map(int, input().split())                
dijkstra(start_city)

print(distances[end_city])