import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

left = 1
right = max(lan)
while left<=right:
    middle = (left + right) // 2
    cnt = 0
    for l in lan:
        cnt += l//middle
        
    if cnt>=N: left = middle + 1
    else: right = middle - 1

print(right)