import sys
import heapq
import collections

input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False for _ in range(V+1)]
graph = collections.defaultdict(list) # 빈 그래프 생성

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, A, B))
    graph[B].append((C, B, A))
    
def prim(start):
    visited[start] = True
    queue = graph[start]
    heapq.heapify(queue)
    
    mst = []
    total_weight = 0
    
    while queue:
        cost, depart, arrive = heapq.heappop(queue)
        
        if not visited[arrive]:
            visited[arrive] = True
            mst.append((depart, arrive))
            total_weight += cost
            
            for next_cost, next_depart, next_arrive in graph[arrive]:
                if not visited[next_arrive]:
                    heapq.heappush(queue, (next_cost, next_depart, next_arrive))
                    
    return total_weight
    
print(prim(1))