import sys, itertools, collections

input = sys.stdin.readline

n = int(input())
population = list(map(int, input().split()))
adjacent = collections.defaultdict(list)
difference = float('inf')

def bfs(combination):
    start = combination[0]
    q = collections.deque([start])
    visited = set([start])
    local_sum = 0
    
    while q:
        v = q.popleft()
        local_sum += population[v]
        for n in adjacent[v]:
            if n not in visited and n in combination:
                q.append(n)
                visited.add(n)
                
    return local_sum, len(visited)

for i in range(n):
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        adjacent[i].append(info[j]-1)     
        
for i in range(1, n//2+1):
    combis = list(itertools.combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if v1+v2==n:
            difference = min(difference, abs(sum1 - sum2))
    
if difference != float('inf'):
    print(difference)
else:
    print(-1)