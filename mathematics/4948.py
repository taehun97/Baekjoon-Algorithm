import sys

input = sys.stdin.readline

def isPrime(num):
    if num==1: return False
    
    for i in range(2, int(num**(1/2))+1):
        if num%i==0: return False
    return True

while True:
    test = int(input())
    
    if test==0: break
    
    cnt = 0
    a, b = test, test*2
    for i in range(a+1, b+1):
        if isPrime(i): cnt += 1
        
    print(cnt)