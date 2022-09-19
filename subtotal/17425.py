import sys

input = sys.stdin.readline

def getDivisors(x):
    divisor_list = []
    for i in range(1, int(x**(1/2)) + 1):
        if x%i==0:
            divisor_list.append(i)
            if x!=i**2: divisor_list.append(x//i)
            
    return divisor_list

T = int(input())
divisor_cumulative_sum = [0 for _ in range(1000001)]
for _ in range(T):
    N = int(input())
    total_sum = 0

    for i in range(1, N+1):
        if divisor_cumulative_sum[i]==0: 
            local_sum = sum(getDivisors(i))
            divisor_cumulative_sum[i] = divisor_cumulative_sum[i-1] + local_sum
        
    print(divisor_cumulative_sum[N])