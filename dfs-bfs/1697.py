import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visit = [0 for _ in range(100001)]
        
def bfs(start, end):
    queue = deque()
    queue.append(start)
    visit[start] = 0    
        
    while queue:
        cur_start = queue.popleft()
        
        if cur_start==end: return visit[cur_start]

        for next_start in [cur_start-1, cur_start+1, cur_start*2]:
            if 0<=next_start<=100000 and not visit[next_start]:
                visit[next_start] = visit[cur_start] + 1
                queue.append(next_start)
            
print(bfs(N, K))