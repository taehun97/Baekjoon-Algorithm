import sys

input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    a, b = map(int, input().split())
    info.append((b, a))
    
info.sort(key = lambda x: (x[0], x[1]))

ans = 1
end_time = info[0][0]
for i in range(1, N):
    if info[i][1]>=end_time:
        end_time = info[i][0]
        ans += 1
print(ans)