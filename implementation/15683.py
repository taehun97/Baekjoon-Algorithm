import sys
import copy

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
blueprint = []
cctv_list = []
direction_combs = [[[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
              [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
              [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]],
              [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)]],
              [[(1, 0), (-1, 0), (0, 1), (0, -1)]]]
unchecked_area = float('inf')

def dfs(cctv_idx, bp):
    global unchecked_area
    
    if cctv_idx==len(cctv_list):
        unchecked_area = min(unchecked_area, calculateUncheckedArea(bp))
        return
    
    cx, cy, num = cctv_list[cctv_idx]
    for directions in direction_combs[num-1]:
        copied_blueprint = copy.deepcopy(bp)
        for (x, y) in directions:
            checkArea(cx, cy, x, y, copied_blueprint)
        dfs(cctv_idx + 1, copied_blueprint)
                

def checkArea(cx, cy, x, y, b):
    if x==0:
        if y>0:
            while cy+y<m:
                if b[cx][cy+y]==0:
                    b[cx][cy+y] = '#'
                    y += 1
                else:
                    if b[cx][cy+y]==6: return
                    else: 
                        y += 1
                        continue
            return
        elif y<0:
            while cy+y>=0:
                if b[cx][cy+y]==0:
                    b[cx][cy+y] = '#'
                    y -= 1
                else:
                    if b[cx][cy+y]==6: return
                    else: 
                        y -= 1
                        continue
            return
    elif y==0:   
        if x>0:
            while cx-x>=0:
                if b[cx-x][cy]==0:
                    b[cx-x][cy] = '#'
                    x += 1
                else:
                    if b[cx-x][cy]==6: return
                    else: 
                        x += 1
                        continue
            return            
        elif x<0:
            while cx-x<n:
                if b[cx-x][cy]==0:
                    b[cx-x][cy] = '#'
                    x -= 1
                else:
                    if b[cx-x][cy]==6: return
                    else: 
                        x -= 1
                        continue
            return
                
def calculateUncheckedArea(b):
    result = 0
    for i in range(n):
        for j in range(m):
            if b[i][j]==0: result += 1
            
    return result
    

for i in range(n):
    row = list(map(int, input().split()))
    blueprint.append(row)    
    for j in range(m):
        if row[j]!=0 and row[j]!=6:
            cctv_list.append((i, j, row[j]))
            
dfs(0, blueprint)
print(unchecked_area)