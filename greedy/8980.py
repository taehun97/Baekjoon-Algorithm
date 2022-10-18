import sys

input = sys.stdin.readline

# N: 마을 수 C: 트력의 용량
N, C = map(int, input().split())
# M: 보내는 박스 정보의 개수
M = int(input())
infos = []
accumulated_sum = [0 for _ in range(N+1)]
village_received_box = [0 for _ in range(N+1)]

def sendBoxCount(limit, box, send, receive, lst):
    capacity = box
    for i in range(send, receive):
        if lst[i] + capacity>limit:
            capacity = limit - lst[i]
    
    return capacity
    
for _ in range(M):
    start, end, box_count = map(int, input().split())
    length = end - start
    # infos.append((length, -box_count, start, end))
    infos.append((end, -box_count, -start))

infos.sort()

for e, cnt, s in infos:
    cnt = abs(cnt)
    s = abs(s)
    box_cnt = sendBoxCount(C, cnt, s, e, accumulated_sum)
    
    for i in range(s, e):
        accumulated_sum[i] += box_cnt
    
    village_received_box[e] += box_cnt
    
# print(village_received_box)
# print(accumulated_sum)
print(sum(village_received_box))

