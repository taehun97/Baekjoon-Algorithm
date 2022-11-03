import sys

input = sys.stdin.readline

alphabet = [0 for _ in range(26)]
BASE = 97

alphabet[ord('a')-BASE] = 1
alphabet[ord('n')-BASE] = 1
alphabet[ord('t')-BASE] = 1
alphabet[ord('i')-BASE] = 1
alphabet[ord('c')-BASE] = 1

N, K = map(int, input().split())

if K<5:
    print(0)
    exit()

words = [list(input().rstrip()) for _ in range(N)]
bitmasking = [[0 for _ in range(26)] for _ in range(N)]

for i in range(N):
    for j in range(len(words[i])):
        element = words[i][j]
        if bitmasking[i][ord(element)-BASE]==0:
            bitmasking[i][ord(element)-BASE] = 1
            
minimum = float('inf')
ary_list = []

for i in range(N):
    cnt = sum(bitmasking[i])
    
    if minimum>cnt:
        minimum = cnt
        ary_list.clear()
        ary_list.append(i)
    elif minimum==cnt:
        ary_list.append(i)
    else: pass
    
