import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    flip_info = list(map(int, list(input().rstrip())))
    info_len = len(flip_info)
    flag = False
    
    if info_len==1: print("YES")
    else:
        while info_len>=3:
            for i in range(info_len//2):
                if flip_info[i]+flip_info[info_len-1-i]!=1:
                    flag = True
                    break
            
            if flag: break
            else:
                flip_info = flip_info[:info_len//2]
                info_len = len(flip_info)
            
        if flag: print("NO")
        else: print("YES")