import sys
from collections import deque

input = sys.stdin.readline

a_max, b_max, c_max = map(int, input().split())
q = deque()
q.append((0, 0))
visited = [[False] * (b_max+1) for _ in range(a_max+1)]
visited[0][0] = True
answer = []

def pour(changed_a, changed_b):
    if not visited[changed_a][changed_b]:
        visited[changed_a][changed_b] = True
        q.append((changed_a, changed_b))
    
def bfs():

    while q:
        cur_a, cur_b = q.popleft()
        cur_c = c_max - cur_a - cur_b
        
        if cur_a == 0:
            answer.append(cur_c)
        
        # a -> b
        water = min(cur_a, b_max - cur_b)
        pour(cur_a - water, cur_b + water)
        
        # a -> c
        water = min(cur_a, c_max - cur_c)
        pour(cur_a - water, cur_b)
        
        # b -> a
        water = min(cur_b, a_max - cur_a)
        pour(cur_a + water, cur_b - water)
                
        # b -> c
        water = min(cur_b, c_max - cur_c)
        pour(cur_a, cur_b - water)
                
        # c -> a
        water = min(cur_c, a_max - cur_a)
        pour(cur_a + water, cur_b)
                
        # c -> b
        water = min(cur_c, b_max - cur_b)
        pour(cur_a, cur_b + water)
                
bfs()

answer.sort()
for i in answer:
    print(i, end=' ')