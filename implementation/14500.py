import sys

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
max_area = 0

for i in range(n):
    for j in range(m-3):
        max_area = max(max_area, paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3])

for i in range(n-3):
    for j in range(m):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])

for i in range(n-1):
    for j in range(m-1):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1])
        
for i in range(1, n):
    for j in range(1, m-1):
        max_area = max(max_area, paper[i][j] + paper[i-1][j] + paper[i][j+1] + paper[i][j-1])
        
for i in range(1, n-1):
    for j in range(0, m-1):
        max_area = max(max_area, paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j+1])
        
for i in range(0, n-1):
    for j in range(1, m-1):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i][j-1] + paper[i][j+1])
        
for i in range(1, n-1):
    for j in range(1, m):
        max_area = max(max_area, paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j-1])        

for i in range(n-2):
    for j in range(m-1):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1])
        
for i in range(n-2):
    for j in range(m-1):
        max_area = max(max_area, paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1])
        
for i in range(n-2):
    for j in range(1, m):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j-1])
        
for i in range(n-2):
    for j in range(1, m):
        max_area = max(max_area, paper[i][j] + paper[i][j-1] + paper[i+1][j-1] + paper[i+2][j-1])
        
for i in range(1, n):
    for j in range(m-2):
        max_area = max(max_area, paper[i][j] + paper[i-1][j] + paper[i-1][j+1] + paper[i-1][j+2])
        
for i in range(n-1):
    for j in range(2, m):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+1][j-2])
        
for i in range(1, n):
    for j in range(2, m):
        max_area = max(max_area, paper[i][j] + paper[i-1][j] + paper[i-1][j-1] + paper[i-1][j-2])
        
for i in range(n-1):
    for j in range(m-2):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2])
        
for i in range(n-2):
    for j in range(m-1):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1])
        
for i in range(n-2):
    for j in range(1, m):
        max_area = max(max_area, paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j-1])
        
for i in range(1, n):
    for j in range(m-2):
        max_area = max(max_area, paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-1][j+2])
        
for i in range(n-1):
    for j in range(m-2):
        max_area = max(max_area, paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2])
        
print(max_area)