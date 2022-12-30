import sys

input = sys.stdin.readline

first = input()
second = input()

first_len = len(first)
second_len = len(second)

dp = [[0 for _ in range(first_len+1)] for _ in range(second_len+1)]

for i in range(1, second_len):
    for j in range(1, first_len):
        if first[j-1]==second[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[second_len-1][first_len-1])

ans = ""
now = dp[second_len-1][first_len-1]
x = first_len-1
y = second_len-1

while now!=0:
    if dp[y][x-1]==now-1 and dp[y-1][x]==now-1:
        ans = first[x-1] + ans
        now -= 1
        y -= 1
        x -= 1
    else:
        if dp[y-1][x]>dp[y][x-1]: y -= 1
        else: x -= 1
print(ans)