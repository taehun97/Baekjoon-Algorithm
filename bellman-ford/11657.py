import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
distance = [float('inf') for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A-1, B-1, C))
    
def bellmanFord(start):

    distance[start] = 0
    
    for i in range(N):
        for start, end, cost in edges:
            if distance[end]>distance[start]+cost:
                distance[end] = distance[start]+cost
                if i==N-1: return True
    return False

isNegative = bellmanFord(0)

if isNegative: print(-1)
else:
    for i in range(1, N):
        if distance[i]==float('inf'): print(-1)
        else: print(distance[i])