n = int(input())
A = list(map(int, input().split()))
reversed_A = A[::-1]
increased = [1 for _ in range(n)]
decreased = [1 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[i]>A[j]:
            increased[i] = max(increased[i], increased[j]+1)
            
        if reversed_A[i]>reversed_A[j]:
            decreased[i] = max(decreased[i], decreased[j]+1)
            
for i in range(n):
    result[i] = increased[i] + decreased[n-i-1] - 1
    
print(max(result))