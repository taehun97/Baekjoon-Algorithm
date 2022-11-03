import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node]<dist: continue
        
        for next_node, d in graph[node]:
            new_distance = distance[node] + d
            if new_distance<distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))
                
    return distance

T = int(input())
for _ in range(T):
    # (교차로, 도로, 목적지 후보) 개수
    n, m, t = map(int, input().split())
    
    # 시작 노드, 교차로1, 교차로2
    start, intersect1, intersect2 = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        
    candidates = []
    for _ in range(t):
        candidates.append(int(input()))
    
    # 시작지점에서 각각의 노드까지의 최단거리 계산
    min_route = dijkstra(start)
    
    min_distance1 = min_route[intersect1]
    min_distance2 = min_route[intersect2]
    
    temp = 0
    # print(min_route)
    must_distance = -1
    for k in range(len(graph[intersect1])):
        if graph[intersect1][k][0]==intersect2:
            must_distance = graph[intersect1][k][1]
    temp_min_route = []
    
    if min_distance1>min_distance2:
        temp += (min_distance2 + must_distance)
        temp_min_route = dijkstra(intersect1)
    else:
        temp += (min_distance1 + must_distance)
        temp_min_route = dijkstra(intersect2)
    
    index = 0
    while index<len(candidates):
        c = candidates[index]
        comp = temp + temp_min_route[c]
        if comp!=min_route[c]:
            candidates.remove(c)
        else: index += 1
    # for c in candidates:
    #     comp = temp + temp_min_route[c]
    #     if comp==min_route[c]:
    #         print(c)
    #         flag = True
    #         break
    
    # 정답 출력
    candidates.sort()
    for e in candidates:
        print(e, end=' ')
    print()
    
    
        
        
    