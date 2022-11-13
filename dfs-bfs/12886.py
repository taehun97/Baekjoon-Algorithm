import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())
answer = False
total_count = A + B + C

if total_count%3!=0:
    answer = False
else:
    check = [[False for _ in range(total_count+1)] for _ in range(total_count+1)]

    low_num = min(A, B, C)
    high_num = max(A, B, C)
    mid_num = A + B + C - low_num - high_num
    
    queue = deque()
    queue.append((low_num, mid_num, high_num))
    check[low_num][mid_num] = True
    
    while queue:
        ln, mn, hn = queue.popleft()
        
        if ln==mn and mn==hn:
            answer = True
            break
        
        # case 1
        temp_ln = ln * 2
        temp_mn = mn
        temp_hn = hn - ln
        
        # case 2
        temp_ln2 = ln * 2
        temp_mn2 = mn - ln
        temp_hn2 = hn        
        
        # case 3
        temp_ln3 = ln
        temp_mn3 = mn * 2
        temp_hn3 = hn - mn
        
        if temp_hn>0:
            next_low_num = min(temp_ln, temp_mn, temp_hn)
            next_high_num = max(temp_ln, temp_mn, temp_hn)
            next_mid_num = total_count - next_low_num - next_high_num
            if not check[next_low_num][next_mid_num]:
                check[next_low_num][next_mid_num] = True
                queue.append((next_low_num, next_mid_num, next_high_num))
                
        if temp_mn2>0:
            next_low_num2 = min(temp_ln2, temp_mn2, temp_hn2)
            next_high_num2 = max(temp_ln2, temp_mn2, temp_hn2)
            next_mid_num2 = total_count - next_low_num2 - next_high_num2
            if not check[next_low_num2][next_mid_num2]:
                check[next_low_num2][next_mid_num2] = True
                queue.append((next_low_num2, next_mid_num2, next_high_num2))
                
        if temp_hn3>0:
            next_low_num3 = min(temp_ln3, temp_mn3, temp_hn3)
            next_high_num3 = max(temp_ln3, temp_mn3, temp_hn3)
            next_mid_num3 = total_count - next_low_num3 - next_high_num3
            if not check[next_low_num3][next_mid_num3]:
                check[next_low_num3][next_mid_num3] = True
                queue.append((next_low_num3, next_mid_num3, next_high_num3))
    
print(0) if not answer else print(1)