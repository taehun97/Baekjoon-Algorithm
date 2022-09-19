import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # Each TestCase
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    next_building_list = [[] for _ in range(N)]
    inDegree = [0 for _ in range(N)]
    dp = [0 for _ in range(N)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        next_building_list[a-1].append(b-1)
        inDegree[b-1] += 1
    
    q = deque()
    for i in range(N):
        if inDegree[i]==0:
            dp[i] = time[i]
            q.append(i)
        
    while q:
        a = q.popleft()
        for next in next_building_list[a]:
            inDegree[next] -= 1
            dp[next] = max(dp[next], dp[a] + time[next])
            if inDegree[next]==0:
                q.append(next)
    
    final_building = int(input()) - 1            
    print(dp[final_building])

