import sys
from collections import Counter

input = sys.stdin.readline

def rc():
    original_row_len = len(A)
    max_len = 0
    
    for i in range(original_row_len):
        temp = [j for j in A[i] if j!=0]
        temp_dic = Counter(temp).most_common()
        temp_dic.sort(key = lambda x : (x[1], x[0]))
        
        A[i] = []
        for key, val in temp_dic:
            A[i].append(key)
            A[i].append(val)
        
        max_len = max(max_len, len(temp_dic)*2)
        
    for i in range(original_row_len):
        for _ in range(max_len-len(A[i])):
            A[i].append(0)
        A[i] = A[i][:100]

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
for i in range(101):
    try:
        if A[r-1][c-1] == k:
            print(i)
            break
    except: pass
    if len(A) < len(A[0]):
        A = list(zip(*A))
        rc()
        A = list(zip(*A))
    else:
        rc()
else:
    print(-1)
