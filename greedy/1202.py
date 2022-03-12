import sys
import heapq

r=sys.stdin.readline

fst_input=list(map(int, r().split()))
n=fst_input[0]
k=fst_input[1]
gems=[]
bags=[]
total_value=0

for i in range(n):
    m, v=tuple(map(int, r().split()))
    heapq.heappush(gems, (m, v))

for i in range(k):
    heapq.heappush(bags, int(r()))

temp_price=[]

while bags:
    bag=heapq.heappop(bags)
    while gems and bag>=gems[0][0]:
        g_m, g_v=heapq.heappop(gems)
        heapq.heappush(temp_price, -g_v)

    if temp_price:
        total_value-=heapq.heappop(temp_price)
    
    if not gems:
        break

print(total_value)