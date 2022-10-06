import sys

input = sys.stdin.readline

n, m = map(int, input().split())
min_mileages = [0 for _ in range(n)]
for i in range(n):
    P, L = map(int, input().split())
    state = list(map(int, input().split()))
    
    state.sort(reverse=True)
    
    if P>=L: min_mileages[i] = state[L-1]
    else: min_mileages[i] = 1

min_mileages.sort()

answer = 0
for mileage in min_mileages:
    m -= mileage
    if m>=0: answer += 1
    else: break
    
print(answer)