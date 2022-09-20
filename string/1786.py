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
while i<len_p:
    # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
    if P[i]==P[leng]:
        leng += 1
        lps[i] = leng
        i += 1
    else:
        # 일치하지 않는 경우
        if leng!=0:
            # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
            leng=lps[leng-1]
            # 다시 검사해야 하므로 i는 증가하지 않음
        else:
            # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
            lps[i] = 0
            i += 1
        
cnt = 0
location = [] 
front = 0
k = 0
while front+len_p<=len_t:
    # print(front)
    isCorrect = True
    for i in range(k, len_p):
        if T[front+i]!=P[i]:
            k = lps[i]
            front += (i - k + 1)
            isCorrect = False
            break
    
    if isCorrect:
        cnt += 1
        location.append(front+1)
        front += len_p
             
print(cnt)
print(*location)