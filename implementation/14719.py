import sys

input = sys.stdin.readline

h, w = map(int, input().split())
maps = [[] for _ in range(h)]

block_info = list(map(int, input().split()))
for i in range(w):
    for j in range(block_info[i]):
        maps[j].append(i)
        
answer = 0
for i in range(h):
    for j in range(0, len(maps[i])-1):
        answer += (maps[i][j+1] - maps[i][j] - 1)
        
print(answer)