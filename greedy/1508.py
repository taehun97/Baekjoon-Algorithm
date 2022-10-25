import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
candidates = list(map(int, input().split()))

start = 0
end = N
answer = ""
while start<=end:
    mid = (start + end)//2
    
    cur_string = "1"
    count = 1
    before = 0
    for i in range(1, K):
        if candidates[i]-candidates[before]>=mid:
            count += 1
            cur_string += "1"
            before = i
            
            if count==M: break
        else: cur_string += "0"
            
    while len(cur_string)<K: cur_string += "0"
            
    if count==M:
        answer = cur_string
        start = mid + 1
    else: end = mid - 1

print(answer)