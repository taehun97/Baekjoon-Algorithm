import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000007

def pow(b, c):
    if c==0: return 1
    elif c%2==1: return (pow(b, c - 1) * b) % MOD
    half = pow(b, c//2) % MOD
    return (half * half) % MOD

A = 1
for i in range(1, N+1):
    A *= i
    A %= MOD
    
B = 1
for i in range(1, K+1):
    B *= i
    B %= MOD
for i in range(1, N-K+1):
    B *= i
    B %= MOD
    
# 페르마의 소정리
# P가 소수이고 P가 A의 배수가 아니라면, A ^ (P - 1) % P = 1이다.
# 이를 활용하여 이항계수에 적용하면 다음과 같다.
# A = n!, B = k! * (n-k)!이라 가정한다면 아래의 식이 성립한다.
# (A / B) % MOD = ((A % MOD) * (B ^ (MOD - 2)) % MOD) % MOD

A %= MOD
B2 = pow(B, MOD-2)

answer = (A * B2) % MOD
print(answer)