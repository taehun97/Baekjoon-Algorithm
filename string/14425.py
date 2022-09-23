import sys

input = sys.stdin.readline

N, M = map(int, input().split())
strings = set([input().rstrip() for _ in range(N)])
cnt = 0

for _ in range(M):
    test_string = input().rstrip()
    if test_string in strings: cnt += 1
    
print(cnt)