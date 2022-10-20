import sys
import math

input = sys.stdin.readline

# def findComparisonIndex(start):
#     for i in range(start-1, -1, -1):
#         if infos[start][1]>infos[i][1]: return i
#     return 0

N = int(input())
infos = [[] for _ in range(N)]
for _ in range(2):
    row = list(map(int, input().split()))
    for i in range(N):
        infos[i].append(row[i])

infos.sort(key = lambda x : (x[1], x[0]))

answer = 0
compIdx = 0
for i in range(N):
    # while infos[i][0]<infos[i][1]:
    #     answer += 1
    #     infos[i][0] += 30
    
    if infos[i][0]<infos[i][1]:
        cnt = math.ceil((infos[i][1] - infos[i][0])/30)
        answer += cnt
        infos[i][0] += 30 * cnt
        
    # idx = findComparisonIndex(i)
    # print(compIdx)
    if i!=0 and infos[i][1]!=infos[0][1]:
        # while infos[compIdx][0]>infos[i][0]:
        #     answer += 1
        #     infos[i][0] += 30
        if infos[compIdx][0]>infos[i][0]:
            cnt2 = math.ceil((infos[compIdx][0]-infos[i][0])/30)
            answer += cnt2
            infos[i][0] += 30 * cnt2
            
        if i!=N-1 and infos[i][1]!=infos[i+1][1]: infos.sort(key = lambda x : (x[1], x[0]))
        
    # print(answer)
    # print(infos)
    
    if i!=N-1 and infos[i][1]<infos[i+1][1]: compIdx = i
        
print(answer)
