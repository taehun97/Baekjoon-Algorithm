import sys

input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))

length.sort()

cnt = len(length) - 2
i = 0
ring_cnt = length[0]
answer = 0
while True:
    if cnt<ring_cnt:
        answer += (cnt + 1)
        break
    elif cnt==ring_cnt:
        answer += cnt
        break
    elif cnt>ring_cnt:
        answer += ring_cnt  
        cnt -= (1 + length[i])
        ring_cnt = length[i+1]
        i += 1
        
print(answer)