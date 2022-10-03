import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

score.sort()

min_sum = float('inf')
for i in range(n):
    min_sum = min(min_sum, score[i] + score[2*n-1-i])
    
print(min_sum)