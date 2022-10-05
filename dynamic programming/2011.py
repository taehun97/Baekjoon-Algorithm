import sys

input = sys.stdin.readline

password = [0] + list(map(int, list(input().rstrip())))
pw_len = len(password)
dp = [1, 1] + [0 for _ in range(pw_len-2)]

if password[1]==0:
    print(0)
    exit()

for i in range(2, pw_len):
    firstNumber = password[i]
    checkNumber = password[i] + password[i-1] * 10
    
    if firstNumber>0: dp[i] += dp[i-1]
    if 10<=checkNumber<=26: dp[i] += dp[i-2]

print(dp[pw_len-1]%1000000)