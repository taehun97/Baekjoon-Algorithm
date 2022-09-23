import sys

input = sys.stdin.readline

def isPrime(num):
    if num==1: return False
    
    for i in range(2, int(num**(1/2))+1):
        if num%i==0: return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i): print(i)