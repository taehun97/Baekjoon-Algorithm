import sys

input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())
a2, b2, c2 = a, b, c
for i in range(1, n):
    a_max, b_max, c_max = map(int, input().split())
    a_min, b_min, c_min = a_max, b_max, c_max
    
    a_max = a_max + max(a, b)
    b_max = b_max + max(a, b, c)
    c_max = c_max + max(b, c)
    
    a_min = a_min + min(a2, b2)
    b_min = b_min + min(a2, b2, c2)
    c_min = c_min + min(b2, c2)
    
    a, b, c = a_max, b_max, c_max
    a2, b2, c2 = a_min, b_min, c_min
    
print(max(a, b, c), min(a2, b2, c2))