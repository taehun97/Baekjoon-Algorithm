import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
cost = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(M):
    city1, city2, length = map(int, input().split())
    graph[city1].append((city2, length))
    graph[city2].append((city1, length))
    
def dijkstra():
    total_cost = [[float('inf') for _ in range(max(cost)+1)] for _ in range(N+1)]
    total_cost[1][cost[1]] = 0
    
    queue = []
    heapq.heappush(queue, (0, cost[1], 1))
    
    while queue:
        cur_cost, oiling_cost, cur_node = heapq.heappop(queue)
        
        if cur_node==N: return cur_cost
        
        if total_cost[cur_node][oiling_cost]<cur_cost: continue
        
        for next_node, next_dist in graph[cur_node]:
            next_cost = min(cost[next_node], oiling_cost)
            
            if total_cost[next_node][oiling_cost]>cur_cost+oiling_cost*next_dist:
                total_cost[next_node][oiling_cost] = cur_cost + oiling_cost * next_dist
                heapq.heappush(queue, (cur_cost + oiling_cost * next_dist, next_cost, next_node))

print(dijkstra())