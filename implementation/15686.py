import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
franchise = []
houses = []
answer = float('inf')

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j]==2:
            franchise.append((i, j))
        elif row[j]==1:
            houses.append((i, j))
    city.append(row)
    
combinations_of_franchise = list(combinations(franchise, m))
    
def calculateMinDistance(combination):
    total_min_distance = 0
    
    for (i, j) in houses:
        min_distance = float('inf')
        for (x, y) in combination:
            local_min_distance = abs(i - x) + abs(j - y)
            if min_distance > local_min_distance:
                min_distance = local_min_distance
            
        total_min_distance += min_distance
                
    return total_min_distance
    
for comb in combinations_of_franchise:
    local_answer = calculateMinDistance(comb)
    if answer > local_answer:
        answer = local_answer
        
print(answer)