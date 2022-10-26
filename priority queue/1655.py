import sys
import heapq

input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []

for i in range(1, N+1):
    num = int(input())
    
    if len(left_heap)==len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and -left_heap[0]>right_heap[0]:
        left_heap_root = -heapq.heappop(left_heap)
        right_heap_root = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_heap_root)
        heapq.heappush(right_heap, left_heap_root)
        
    print(-left_heap[0])