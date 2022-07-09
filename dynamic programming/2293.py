n, k = map(int, input().split())
values = []
num_of_cases = [0 for i in range(k+1)]
num_of_cases[0] = 1
        
for _ in range(n):
    values.append(int(input()))
    
for value in values:
    for i in range(value, k+1):
        num_of_cases[i] += num_of_cases[i-value]
    
print(num_of_cases[-1])

