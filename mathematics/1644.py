import sys

input = sys.stdin.readline

N = int(input())

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num%i==0: return False
    return True

prime_list = []
for i in range(2, N+1):
    if isPrime(i): prime_list.append(i)

answer = 0    
len_p = len(prime_list)

# Solution 1
# for i in range(len_p):
#     sum = 0
#     for j in range(i, len_p):
#         sum += prime_list[j]
#         if sum==N:
#             answer += 1
#             break
#         elif sum>N: break

# Solution 2
front, back = 0, 1
while front<len_p:
    prime_subtotal = sum(prime_list[front:back])
    if prime_subtotal==N:
        answer += 1
        front += 1
    elif prime_subtotal<N:
        if back<len_p: back += 1
        else: front += 1
    else:
        front += 1
        
print(answer)
        
    
