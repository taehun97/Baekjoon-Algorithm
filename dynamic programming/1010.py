import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # M combination N
    
    factorial = [1 for _ in range(M+1)]
    for i in range(2, M+1):
        factorial[i] = factorial[i-1] * i
        
    answer = factorial[M] // (factorial[N] * factorial[M-N])
    print(answer)