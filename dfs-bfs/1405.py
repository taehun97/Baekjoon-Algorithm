import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4방향 탐색
n, percent_e, percent_w, percent_s, percent_n = map(int, input().split())
prob = [percent_e / 100, percent_w / 100, percent_s / 100, percent_n / 100]

result = 0

def dfs(path_log, step, total):
    global result
    
    if step==0:
        result += total
        return
    
    x, y = path_log[-1]
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]

        if (nx, ny) not in path_log:
            path_log.append((nx, ny))
            dfs(path_log, step - 1, total * prob[i])
            path_log.pop()
        
dfs([(0, 0)], n, 1)

print(result)