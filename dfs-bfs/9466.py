import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(obj):
    global team
    
    route.append(obj)
    visited[obj] = 1
    next = choice[obj]
    
    if visited[next]:
        if next in route:
            team += route[route.index(next):]
        return
    
    dfs(next)
            
case = int(input())

for _ in range(case):
    team = []
    num_of_student = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [1] + [0] * num_of_student
    
    for i in range(1, num_of_student + 1):
        if not visited[i]:
            route = []
            dfs(i)
            
    print(num_of_student - len(team))