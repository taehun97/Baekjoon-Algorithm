import sys
from collections import deque

input = sys.stdin.readline

def bfs(s1, s2, s3):
    dq = deque()
    dq.append([len(s1), len(s2), len(s3)])
    visited = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    
    while dq:
        l1, l2, l3 = dq.popleft()
        
        if l1==0 and l2==0 and l3==0: return True
        
        if l1>0 and s1[l1-1]==s3[l3-1] and not visited[l1-1][l2]:
            visited[l1-1][l2] = True
            dq.append([l1 - 1, l2, l3 - 1])
        if l2>0 and s2[l2-1]==s3[l3-1] and not visited[l1][l2-1]:
            visited[l1][l2-1] = True
            dq.append([l1, l2 - 1, l3 - 1])
            
    return False

N = int(input())
for test_case in range(1, N+1):
    str1, str2, str3 = map(str, input().split())
    
    isPossible = bfs(str1, str2, str3)
    
    if isPossible: print("Data set " + str(test_case) + ": yes")
    else: print("Data set " + str(test_case) + ": no")
    

            
