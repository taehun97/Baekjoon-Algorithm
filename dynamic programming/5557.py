import sys

input = sys.stdin.readline

n = int(input())
integer_list = list(map(int, input().split()))
integers = integer_list[:-1]
result = integer_list[-1]
dp = [[0 for _ in range(21)] for _ in range(n-1)]

dp[0][integers[0]] += 1
q = set([])
q.add(integers[0])

for i in range(1, n-1):
    temp_q = set([])
    for element in q:
        local_max = element + integers[i]
        local_min = element - integers[i]
        
        if local_max<=20:
            temp_q.add(local_max)
            dp[i][local_max] += dp[i-1][element]
            
        if local_min>=0:
            temp_q.add(local_min)
            dp[i][local_min] += dp[i-1][element]
            
    q = temp_q
    
print(dp[-1][result])

    