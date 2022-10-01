import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(r)]
entry = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
prev_rank = 0
rank = [0 for _ in range(10)]

for i in range(c-2, 0, -1):
    flag = False
    for j in range(r):
        if maps[j][i] in entry:
            rank[int(maps[j][i])] = prev_rank + 1
            entry.remove(maps[j][i])
            if not flag: flag = True
    
    if flag: prev_rank += 1

for i in range(1, 10):
    print(rank[i])