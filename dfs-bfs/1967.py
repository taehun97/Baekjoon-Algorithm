import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
diameter = 0

def dfs(cur, val):
    
    left, right = 0, 0
    for dst, value in graph[cur]:
        v = dfs(dst, value)
        if left <= right:
            left = max(left, v)
        else:
            right = max(right, v)
            
    global diameter
    diameter = max(diameter, left + right)
    return max(left + val, right + val)

for _ in range(n-1):
    v1, v2, value = map(int, input().split())
    graph[v1].append((v2, value))
    
dfs(1, 0)
print(diameter)