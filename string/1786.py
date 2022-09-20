import sys

input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()
len_t = len(T)
len_p = len(P)

# LPS 계산
lps = [0 for _ in range(len_p)]
leng = 0  # length of the previous longest prefix suffix

# 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
i = 1
while i<len_p: # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
    if P[leng]==P[i]:
        leng += 1
        lps[i] = leng
        i += 1
    else: # 일치하지 않는 경우
        if leng!=0: # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
            leng=lps[leng-1]
            # 다시 검사해야 하므로 i는 증가하지 않음
        else: # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
            lps[i] = 0
            i += 1

# KMP 알고리즘        
cnt = 0
location = [] 
t_idx = 0
p_idx = 0
while t_idx<len_t:
    if T[t_idx]==P[p_idx]:
        t_idx += 1
        p_idx += 1
    else:
        if p_idx!=0:
            p_idx = lps[p_idx-1]
        else:
            t_idx += 1
    
    if p_idx==len_p:
        cnt += 1
        location.append(t_idx-len_p+1)
        p_idx = lps[p_idx-1]
        
print(cnt)
print(*location)
        