import sys
import heapq

input = sys.stdin.readline
n = int(input())
card_chunks = []
for _ in range(n):
    heapq.heappush(card_chunks, int(input()))

answer = 0
while len(card_chunks)!=1:
    min_first = heapq.heappop(card_chunks)
    min_second = heapq.heappop(card_chunks)
    
    answer += (min_first + min_second)
    heapq.heappush(card_chunks, min_first + min_second)
    
print(answer)