import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

while len(T)!=len(S):
    if T[-1]=='A':
        T = T[:-1]
    elif T[-1]=='B':
        T = T[:-1]
        T = T[::-1]
        
print(1) if S==T else print(0)