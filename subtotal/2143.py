import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

answer = 0
sumA = []
sumB = []

for i in range(n):
    s = A[i]
    sumA.append(s)
    for j in range(i+1, n):
        s += A[j]
        sumA.append(s)
        
for i in range(m):
    s = B[i]
    sumB.append(s)
    for j in range(i+1, m):
        s += B[j]
        sumB.append(s)
        
sumA.sort()
sumB.sort()

for i in range(len(sumA)):
    remain = t - sumA[i]
    l = bisect_left(sumB, remain)
    r = bisect_right(sumB, remain)
    answer += r - l

print(answer)