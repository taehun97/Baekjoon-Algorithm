import sys

input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in range(N):
    students[i] -= B
    if students[i]>0: answer += (students[i]//C if students[i]%C==0 else students[i]//C+1)
        
print(answer)