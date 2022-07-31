import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cleaning_cnt = 0

n, m = map(int, input().split())
start_x, start_y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[False]*m for _ in range(n)]

def cleaningRule(cur_x, cur_y, cur_d, num_of_rotation):
    global cleaning_cnt
    
    if not cleaned[cur_x][cur_y]: 
        cleaned[cur_x][cur_y] = True
        cleaning_cnt += 1
    
    if num_of_rotation==4:
        m_x, m_y = direction[(cur_d + 2) % 4]
        if maps[cur_x + m_x][cur_y + m_y]==1:
            return
        else: 
            cleaningRule(cur_x + m_x, cur_y + m_y, cur_d, 0)
            return
    
    new_d = (cur_d - 1)%4
    new_d_x, new_d_y = direction[new_d][0], direction[new_d][1]
    new_x, new_y = cur_x + new_d_x, cur_y + new_d_y
    
    if maps[new_x][new_y]==0 and not cleaned[new_x][new_y]:
        cleaningRule(new_x, new_y, new_d, 0)
        return
    else:
        cleaningRule(cur_x, cur_y, new_d, num_of_rotation + 1)
        return

cleaningRule(start_x, start_y, d, 0)
print(cleaning_cnt)