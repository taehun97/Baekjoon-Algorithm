import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = [0] + list(map(int, input().split()))

accumulative_num = [0 for _ in range(N+1)]
for i in range(1, N+1):
    accumulative_num[i] = accumulative_num[i-1] + num[i]
    
for _ in range(M):
    i, j = map(int, input().split())
    subtotal = accumulative_num[j] - accumulative_num[i-1]
    
    print(subtotal)