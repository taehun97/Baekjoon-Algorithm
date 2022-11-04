import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
distance = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start-1][end-1] = min(cost, graph[start-1][end-1])
    
for i in range(n):
    for j in range(n):
        if i!=j:
            if graph[i][j]!=float('inf'): distance[i][j] = graph[i][j]
            else: pass
        else: distance[i][j] = 0
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(n):
    for j in range(n):
        if distance[i][j]==float('inf'): print(0, end = ' ')
        else: print(distance[i][j], end = ' ')
    print()