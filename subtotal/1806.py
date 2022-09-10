import sys

input = sys.stdin.readline

n, s = map(int, input().split())
ary = list(map(int, input().split()))
sum = ary[0]
answer = 100001
i, j = 0, 0

while True:
    if sum>=s:
        sum -= ary[i]
        answer = min(answer, j - i + 1)
        i += 1
    else:
        j += 1
        if j==n: break
        sum += ary[j]

print(0) if answer==100001 else print(answer)
    