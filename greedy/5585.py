import sys

input = sys.stdin.readline

pennies = [500, 100, 50, 10, 5, 1]
pay = int(input())
remain = 1000 - pay

answer = 0

for p in pennies:
    answer += remain//p
    remain %= p

print(answer)