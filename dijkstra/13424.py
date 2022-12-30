import sys
import heapq

input = sys.stdin.readline

def dijkstra(n, g, start):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        
        if distance[cur_node]<cur_dist: continue
        
        for next_node, next_dist in g[cur_node]:
            new_distance = next_dist + cur_dist
            if distance[next_node]>new_distance:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance

test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    friend = int(input())
    start_location = list(map(int, input().split()))
    
    ans = float('inf')
    room_num = 0
    for i in range(1, N+1):
        distances = dijkstra(N, graph, i)
        local_ans = 0
        for room in start_location:
            local_ans += distances[room]
        
        if local_ans<ans:
            ans = local_ans
            room_num = i
        
    print(room_num)