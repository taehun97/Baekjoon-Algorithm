import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, n, m):
    distance = [[float('inf') for _ in range(n)] for _ in range(m+1)]
    queue = []
    heapq.heappush(queue, (0, 0, start))
    
    while queue:
        curDist, curCost, curNode = heapq.heappop(queue)
        
        if distance[curCost][curNode]<curDist: continue
        
        for nextNode, nextCost, nextDist in graph[curNode]:
            newCost = curCost + nextCost
            newDist = curDist + nextDist
            if newCost<=m and newDist<distance[newCost][nextNode]:
                for i in range(newCost, m+1):
                    if distance[i][nextNode]>newDist:
                        distance[i][nextNode] = newDist
                    else: break
                heapq.heappush(queue, (newDist, newCost, nextNode))
    return distance

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    
    graph = [[] for _ in range(N)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u-1].append((v-1, c, d))
        
    distances = dijkstra(0, N, M)
    
    if distances[M][N-1]==float('inf'): print("Poor KCM")
    else: print(distances[M][N-1])
        