import sys

input = sys.stdin.readline

N, H = map(int, input().split())
up = [0 for _ in range(H+1)]
down = [0 for _ in range(H+1)]
min_cnt = N
range_cnt = 0

for i in range(1, N+1):
    if i%2==0: up[int(input())] += 1
    else: down[int(input())] += 1

for i in range(H, 1, -1):
    up[i-1] += up[i]
    down[i-1] += down[i]
    
for i in range(1, H+1):
    if min_cnt>up[i]+down[H-i+1]:
        min_cnt = up[i]+down[H-i+1]
        range_cnt = 1
    elif min_cnt==up[i]+down[H-i+1]:
        range_cnt += 1
        
print(min_cnt, range_cnt)