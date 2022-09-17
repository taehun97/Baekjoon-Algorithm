import sys
import re

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    spread = input().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(spread)
    
    print("YES") if m else print("NO")