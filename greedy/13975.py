import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    file = list(map(int, input().split()))
    answer = 0
    heap = []
    
    for element in file:
        heapq.heappush(heap, element)
    
    while True:
        if len(heap)==1: break
        
        min_value1 = heapq.heappop(heap)
        min_value2 = heapq.heappop(heap)
        
        local_min = min_value1 + min_value2
        heapq.heappush(heap, local_min)
        answer += local_min
        
    print(answer)