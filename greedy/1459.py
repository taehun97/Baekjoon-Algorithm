import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())
answer = 0

if w*2>s: answer += min(x, y) * s
else: answer += min(x, y) * w * 2
    
if w>s: answer += (abs(x - y) // 2) * 2 * s + (abs(x - y) % 2) * w
else: answer += abs(x - y) * w
    
print(answer)