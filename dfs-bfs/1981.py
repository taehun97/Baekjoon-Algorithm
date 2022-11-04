import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
board = []
visited = [[0 for _ in range(n)] for _ in range(n)]
visit_cnt = 0
lst = set()
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    
    for j in range(n):
        lst.add(row[j])
        
num_list = sorted(list(lst))

def bfs(low, high):
    global visited, visit_cnt
    
    if board[0][0]<low or board[0][0]>high: return False
    
    queue = deque()
    queue.append((0, 0))
    visit_cnt += 1
    visited[0][0] = visit_cnt
    
    while queue:
        x, y = queue.popleft()
        
        if x==n-1 and y==n-1:
            return True
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]!=visit_cnt and low<=board[nx][ny]<=high:
                visited[nx][ny] = visit_cnt
                queue.append((nx, ny))
                
    return False

left, right = 0, 0
answer = float('inf')

while 0<=left<len(num_list) and 0<=right<len(num_list):
    if bfs(num_list[left], num_list[right]):
        if left==right:
            print(0)
            exit()
        else:
            answer = min(answer, abs(num_list[right] - num_list[left]))
            left += 1
    else:
        right += 1
        
print(answer)