import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    answer = 0
    max_idx = N-1
    
    for i in range(N-2, -1, -1):
        if price[max_idx]<=price[i]: max_idx = i
        else: answer += (price[max_idx] - price[i])
        
    print(answer)