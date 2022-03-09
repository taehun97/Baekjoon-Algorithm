import sys

num=int(sys.stdin.readline())
s=set()
    
for i in range (num):
    storage=sys.stdin.readline().strip().split()
    if len(storage)==1:
        if storage[0]=="all":
            s=set([i for i in range (1, 21)])
        elif storage[0]=="empty":
            s=set()
    else:    
        if storage[0]=="add":
            s.add(int(storage[1]))
        elif storage[0]=="remove":
            s.discard(int(storage[1]))
        elif storage[0]=="check":
            if int(storage[1]) in s:
                print(1)
            else:
                print(0)
        elif storage[0]=="toggle":
            if int(storage[1]) in s:
                s.discard(int(storage[1]))
            else:
                s.add(int(storage[1]))