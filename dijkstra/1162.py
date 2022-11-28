import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
# 1 -> N
def dijkstra():
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    costs = []
    
    queue = []
    heapq.heappush(queue, (0, 1, []))
    
    while queue:
        dist, cur_node, cur_costs = heapq.heappop(queue)
        
        if cur_node==N:
            costs.append(cur_costs)
            
        if distance[cur_node]<dist: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = next_dist + dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node, cur_costs + [next_dist]))
    return costs

costs = dijkstra()

answer = float('inf')
for cost in costs:
    idx_list = []
    for _ in range(K):
        max_cost = -float('inf')
        max_idx = 0
        for i in range(len(cost)):
            if i in idx_list: continue
            max_cost = max(max_cost, cost[i])
            max_idx = i
        idx_list.append(max_idx)
    # print(idx_list)
    total_cost = 0
    for p in range(len(cost)):
        if p not in idx_list:
            total_cost += cost[p]
    answer = min(answer, total_cost)
    # print(answer)
    
print(answer)
    