import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
remain = [0 for _ in range(M)]
ans = 0
remain[0] = 1
sum = 0

for i in range(N):
    sum += A[i]
    remain[sum%M] += 1
    
for r in remain:
    ans += r*(r-1)//2

print(ans)    