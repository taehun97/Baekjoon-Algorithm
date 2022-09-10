import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ary = [input().rstrip() for _ in range(n)]
    
    ary.sort()
    
    print(ary)
    
    flag = True
    for i in range(len(ary)-1):
        if ary[i]==ary[i+1][:len(ary[i])]:
            flag = False
            break
        else: print(ary[i+1][:len(ary[i])])
    
    print("YES") if flag else print("NO")
        