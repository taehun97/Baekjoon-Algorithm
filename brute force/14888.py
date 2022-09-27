from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
temp = list(map(int, input().split()))
operator = []

for i in range(4):
    for c in range(temp[i]):
        operator.append(i)

max_result = -float('inf')
min_result = float('inf')
operator_perms = list(set(list(permutations(operator, len(operator)))))
for perm in operator_perms:
    result = numbers[0]
    for i in range(len(perm)):
        if perm[i]==0:
            result += numbers[i+1]
        elif perm[i]==1:
            result -= numbers[i+1]
        elif perm[i]==2:
            result *= numbers[i+1]
        else:
            if result>=0:
                result = result//numbers[i+1]
            else:
                result = -(abs(result)//numbers[i+1])
                
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    
print(max_result)
print(min_result)