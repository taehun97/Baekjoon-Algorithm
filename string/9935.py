import sys

input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []
lastChar = bomb[-1]
length = len(bomb)

for e in string:
    stack.append(e)
    if e==lastChar and ''.join(stack[-length:])==bomb:
        del stack[-length:]
        
answer = ''.join(stack)

if answer=='':
    print("FRULA")
else:
    print(answer)
