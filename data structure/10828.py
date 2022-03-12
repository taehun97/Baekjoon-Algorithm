import sys
from collections import deque

num=int(input())
stack=deque()
memory=[]

for i in range (num):
    memory.append(sys.stdin.readline())
    
for i in range (num):
    memory[i]=memory[i].strip('\n')
    if memory[i]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif memory[i]=="size":
        print(len(stack))
    elif memory[i]=="empty":
        print(1 if len(stack)==0 else 0)
    elif memory[i]=="top":
        if len(stack)!=0:
            temp=stack.pop()
            print(temp)
            stack.append(temp)
        else:
            print(-1)
    else:
        cmd=memory[i].split(' ')
        if cmd[0]=="push":
            stack.append(int(cmd[1]))