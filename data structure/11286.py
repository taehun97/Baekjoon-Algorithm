import sys
import heapq

num=int(sys.stdin.readline())
heap=[]

for i in range (num):
    temp=int(sys.stdin.readline())
    if temp!=0:
        heapq.heappush(heap, (abs(temp), temp))
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
        