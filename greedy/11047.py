import sys
import heapq

r=sys.stdin.readline

fst_input=list(map(int, r().split()))
n=fst_input[0]
k=fst_input[1]

moneys=[]
min_cnt=0

for _ in range(n):
    heapq.heappush(moneys, -int(r()))

for _ in range (n):
    money=-heapq.heappop(moneys)
    if k//money!=0:
        min_cnt+=k//money
        k=k%money      
    if k==0: break
    
print(min_cnt)