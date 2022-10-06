import sys

input = sys.stdin.readline

N = int(input())
dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

front, back = map(int, input().split())

length = int(input())
use_order = []
for _ in range(length):
    use_order.append(int(input()))

# DP solution
def solve(idx, f, b):
    if idx==length: return 0
    
    use = use_order[idx]
    dp[use][f][b] = min(abs(f-use) + solve(idx+1, use, b), 
                        abs(b-use) + solve(idx+1, f, use))
    
    return dp[use][f][b]

print(solve(0, front, back))



# DFS solution
# answer = float('inf')

# def dfs(idx, f, b, cnt):
#     global answer
    
#     if idx==length: 
#         answer = min(answer, cnt)
#         return
        
#     use = use_order[idx]
    
#     if f<use<b:
#         dfs(idx+1, use, b, cnt + abs(f-use))
#         dfs(idx+1, f, use, cnt + abs(b-use))
#     elif use<=f:
#         dfs(idx+1, use, b, cnt + abs(f-use))
#     elif use>=b:
#         dfs(idx+1, f, use, cnt + abs(b-use))
        
# dfs(0, front, back, 0)

# print(answer)