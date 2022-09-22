import sys

input = sys.stdin.readline

N = int(input())
P = "I" + "OI" * N
len_p = len(P)

M = int(input())
S = input().rstrip()

lps = [0 for _ in range(len_p)]
j = 0
for i in range(1, len_p):
    while j>0 and P[i]!=P[j]:
        j = lps[j-1]
    if P[i]==P[j]:
        j += 1
        lps[i] = j
        
idx_p = 0
idx_s = 0
cnt = 0
while idx_s<M:
    if P[idx_p]==S[idx_s]:
        idx_p += 1
        idx_s += 1
    else:
        if idx_p!=0:
            idx_p = lps[idx_p-1]
        else:
            idx_s += 1
    
    if idx_p==len_p:
        cnt += 1
        idx_p = lps[idx_p-1]
        
print(cnt)
    