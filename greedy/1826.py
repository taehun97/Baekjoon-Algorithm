import sys
import heapq

input = sys.stdin.readline

N = int(input())
fuel_infos = []

for _ in range(N+1):
    distance, fuel = map(int, input().split())
    fuel_infos.append((distance, fuel))
    
fuel_infos.sort(key = lambda x : x[0])
        
answer = 0
heap = []
cur_location = 0
cur_fuel = fuel_infos[-1][1]

for i in range(N+1):
    dist = fuel_infos[i][0] - cur_location
    cur_location = fuel_infos[i][0]
    
    if cur_fuel<dist:
        while cur_fuel<dist:
            if len(heap)>0:
                cur_fuel += (-1 * heapq.heappop(heap))
                answer += 1
            else:
                answer = -1
                break
        if answer==-1: break
            
    cur_fuel -= dist
    heapq.heappush(heap, -fuel_infos[i][1])
            
print(answer)
    
            
            
    
