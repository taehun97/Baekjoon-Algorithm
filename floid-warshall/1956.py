import sys
import heapq

input = sys.stdin.readline

# Floid-Warshall Solution
# V, E = map(int, input().split())
# distance = [[float('inf') for _ in range(V)] for _ in range(V)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     distance[a-1][b-1] = c
        
# for k in range(V):
#     for i in range(V):
#         for j in range(V):
#             if distance[i][j]>distance[i][k]+distance[k][j]:
#                 distance[i][j] = distance[i][k] + distance[k][j]

# answer = float('inf')
# for i in range(V):
#     if distance[i][i]!=float('inf') and answer>distance[i][i]: answer = distance[i][i]
    
# if answer==float('inf'): print(-1)
# else: print(answer)

# Dijkstra Solution
V, E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    
def dijkstra(start):
    distance = [float('inf') for _ in range(V)]
    
    start_distance = float('inf')
    for n, d in graph[start]:
        if n==start:
            start_distance = d
            break
    
    distance[start] = 0 if start_distance==float('inf') else start_distance
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, cur_node = heapq.heappop(queue)
        
        if dist>distance[cur_node]: continue
        
        for next_node, next_dist in graph[cur_node]:
            new_distance = dist + next_dist
            
            if new_distance<distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance

result = []
for i in range(V):
    result.append(dijkstra(i))
    
answer = [float('inf') for _ in range(V)]
for i in range(V):
    local_answer = float('inf')
    for j in range(i, V):
        if i==j:
            local_answer = min(local_answer, result[i][i] if result[i][i]!=0 else float('inf'))
        else:
            local_answer = min(local_answer, result[i][j] + result[j][i])
    answer[i] = local_answer        
    
a = min(answer)
print(a) if a!=float('inf') else print(-1)