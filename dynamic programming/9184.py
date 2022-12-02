import sys

input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        dp[0][i][j] = 1
        
for i in range(21):
    for j in range(21):
        dp[i][0][j] = 1
        
for i in range(21):
    for j in range(21):
        dp[i][j][0] = 1
        
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i<j<k: dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else: dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
            
while True:
    a, b, c = map(int, input().split())
    temp_a, temp_b, temp_c = a, b, c
    
    if a==-1 and b==-1 and c==-1: break
 
    if a>20 or b>20 or c>20:
        temp_a = 20
        temp_b = 20
        temp_c = 20
    
    if a<=0: temp_a = 0
    if b<=0: temp_b = 0
    if c<=0: temp_c = 0
    

    print("w(%d, %d, %d) = %d" %(a, b, c, dp[temp_a][temp_b][temp_c]))