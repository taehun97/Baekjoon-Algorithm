t = int(input())
result = []

for _ in range(t):
    n = int(input())
    costs = list(map(int, input().split()))
    total_value = int(input())
    
    num_of_cases=[0 for _ in range(total_value+1)]
    num_of_cases[0]=1
    
    for cost in costs:
        for i in range(cost, total_value+1):
            num_of_cases[i] += num_of_cases[i-cost]
    result.append(num_of_cases[-1])
    
for i in range(len(result)):
    print(result[i])        
    
    