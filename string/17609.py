import sys

input = sys.stdin.readline

T = int(input())
# DP Solution
# for _ in range(T):
#     string = input().rstrip()
#     str_len = len(string)
#     dp = [[-1]*str_len for _ in range(str_len)]
    
#     for i in range(str_len):
#         for j in range(str_len-i):
#             if i==0: dp[j][j+i] = 0
#             elif i==1:
#                 if string[j]==string[j+i]: dp[j][j+i] = 0
#                 else: dp[j][j+i] = 1
#             else:
#                 if string[j]==string[j+i]:
#                     if dp[j+1][j+i-1]==0: dp[j][j+i] = 0
#                     elif dp[j+1][j+i-1]==1: dp[j][j+i] = 1
#                     else: dp[j][j+i] = 2
#                 else:
#                     if dp[j][j+i-1]==0 or dp[j+1][j+i]==0: dp[j][j+i] = 1
#                     else: dp[j][j+i] = 2                    
#     print(dp[0][-1])

# String Solution
for _ in range(T):
    string = input().rstrip()
    str_len = len(string)
    front, back = 0, str_len - 1
    check = 0
    
    while True:
        if front>back: break
        
        if string[front]==string[back]:
            front += 1
            back -= 1
            continue

        if string[front]==string[back-1]:
            sub_string = string[front:back]
            if sub_string[:]==sub_string[::-1]:
                check = 1
                break

        if string[front+1]==string[back]:
            sub_string = string[front+1:back+1]
            if sub_string[:]==sub_string[::-1]:
                check = 1
                break

        check = 2
        break
    
    print(check)
        