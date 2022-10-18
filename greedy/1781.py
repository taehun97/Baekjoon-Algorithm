import sys
import heapq

input = sys.stdin.readline

N = int(input())
infos = []
for _ in range(N):
    deadline, score = map(int, input().split())
    infos.append((deadline, score))
    
infos.sort()

heap = []
for i in range(N):
    deadline = infos[i][0]
    score = infos[i][1]
    
    if deadline>len(heap):
        heapq.heappush(heap, score)
    else:
        heapq.heappop(heap) # 힙 안에 있는 수 중 제일 작은 수를 내보냄
        heapq.heappush(heap, score)
    
print(sum(heap))