import sys

input = sys.stdin.readline

N, K = map(int, input().split())
N = list(str(N))
answer = -1

def isDuplicatedNumber(lst):
    for i in range(len(lst)-1):
        if int(lst[i])==int(lst[i+1]): return True
    return False

def findAppropriateIndices(lst):
    for i in range(len(lst)-2, -1, -1):
        if not(i==0 and int(lst[i+1])==0): return i, i+1
    return -1, -1

def dfs(idx, cnt):
    global answer
    
    if cnt==K:
        answer = max(answer, int(''.join(N)))
        return
    
    for start_idx in range(idx, len(N)-1):
        for swap_idx in range(start_idx+1, len(N)):
            if start_idx==0 and int(N[swap_idx])==0: continue
            if int(N[start_idx])<int(N[swap_idx]):
                N[start_idx], N[swap_idx] = N[swap_idx], N[start_idx]
                dfs(start_idx, cnt + 1)
                N[start_idx], N[swap_idx] = N[swap_idx], N[start_idx]
                
    if cnt<K:
        if isDuplicatedNumber(N):
            dfs(idx, K)
        else:
            idx1, idx2 = findAppropriateIndices(N)
            
            if idx1==-1 and idx2==-1:
                print(-1)
                exit()
            else:
                additionalSwap = (K - cnt) % 2
                if additionalSwap==1:
                    N[idx1], N[idx2] = N[idx2], N[idx1]
                    dfs(idx, K)
                    N[idx1], N[idx2] = N[idx2], N[idx1]
                else: dfs(idx, K)

dfs(0, 0)
    
print(answer)