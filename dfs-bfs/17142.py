import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
laboratory = []
virus_candidates = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = float('inf')

for i in range(N):
    row = list(map(int, input().split()))
    laboratory.append(row)
    for j in range(N):
        if row[j]==2: virus_candidates.append((i, j))
        
def getSpreadTime(c):
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    result = -float('inf')
    unchosed_virus_list = set(virus_candidates) - set(comb)
    
    for x, y in c:
        visited[x][y] = True
        queue.append((x, y, 0))
        
    while queue:
        cx, cy, elapsed_time = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and laboratory[nx][ny]!=1:
                visited[nx][ny] = True
                queue.append((nx, ny, elapsed_time+1))
        
        if (cx, cy) not in unchosed_virus_list: result = max(result, elapsed_time)
        
    return result, isAllSpread(visited)

def isAllSpread(v):
    for i in range(N):
        for j in range(N):
            if not v[i][j] and laboratory[i][j]!=1:
                return False
    return True

comb_list = list(combinations(virus_candidates, M))
for comb in comb_list:
    local_min_time, all_spread = getSpreadTime(comb)
    if all_spread: answer = min(answer, local_min_time)
    
if answer==float('inf'): print(-1)
else: print(answer)