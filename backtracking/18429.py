import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().split())
workout_kit = list(map(int, input().split()))
visited = [False for _ in range(n)]
case = 0

workout_cases = permutations(workout_kit)

def backtracking(v_nodes, weight):
    global case
    
    if len(v_nodes)==n:
        case += 1
        return
    
    for i in range(n):
        if (i, workout_kit[i]) in v_nodes: continue
        
        if not visited[i]:
            if weight+workout_kit[i]-k<500: continue
            else:
                v_nodes.append((i, workout_kit[i]))
                visited[i]==True
                
                backtracking(v_nodes, weight + workout_kit[i] - k)
                
                v_nodes.pop()
                visited[i]==False
                

backtracking([], 500)
print(case)