import sys

input = sys.stdin.readline

N, M = map(int, input().split())
relation = [[False for _ in range(N)] for _ in range(N)]
distance = [[float('inf') for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a-1][b-1] = True
    distance[a-1][b-1] = 1
    
    relation[b-1][a-1] = True
    distance[b-1][a-1] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][j]>distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                
for row in distance:
    print(*row)
                
ans = float('inf')
min_num = float('inf')
for i in range(N):
    total_distance = sum(distance[i])
    
    if min_num>total_distance:
        min_num = total_distance
        ans = i + 1
        
print(ans)