n, k = map(int, input().split())
min_count=[10001 for _ in range(0, k+1)]
min_count[0]=0
values = []
for _ in range(n):
    values.append(int(input()))
    
for value in values:
    for i in range(value, k+1):
        min_count[i] = min(min_count[i], min_count[i-value]+1)

if min_count[k]==10001: print(-1)
else: print(min_count[-1])