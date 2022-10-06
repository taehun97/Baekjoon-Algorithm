import sys

input = sys.stdin.readline

N = int(input())
expected_rank = [0]
for _ in range(N):
    expected_rank.append(int(input()))
    
expected_rank.sort()

anger = 0
for i in range(1, N+1):
    anger += abs(i-expected_rank[i])

print(anger)