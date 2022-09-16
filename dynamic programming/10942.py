import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(0, n-i):
        if i==0: dp[j][j+i] = 1
        elif i==1:
            if num[j]==num[j+i]: dp[j][j+i] = 1
            else: dp[j][j+i] = 0
        else:
            if num[j]==num[j+i] and dp[j+1][j+i-1]==1: dp[j][j+i] = 1
            else: dp[j][j+i] = 0

for _ in range(m):
    front, back = map(int, input().split())
    print(dp[front-1][back-1])