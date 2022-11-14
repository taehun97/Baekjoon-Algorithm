import sys

input = sys.stdin.readline

BASE = ord('a')

N, K = map(int, input().split())
words = [list(input().rstrip()) for _ in range(N)]
answer = 0

def dfs(idx, cnt):
    global answer
    
    if cnt==K-5:
        count = 0
        for word in words:
            flag = True
            for w in word:
                if not check[ord(w) - BASE]:
                    flag = False
                    break
            
            if flag: count += 1
            
        answer = max(answer, count)
        
    for i in range(idx, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False

if K<5: print(0)
elif K==26: print(N)
else:
    check = [False for _ in range(26)]
    
    for c in ('a', 'c', 'i', 'n', 't'):
        check[ord(c) - BASE] = True
        
    dfs(0, 0)
    print(answer)
    
        