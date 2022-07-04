import sys

r=sys.stdin.readline
grid=[]
cnt=[5, 5, 5, 5, 5]
total_cnt=0
exitFlag=False 

# fill out the grid
for _ in range (10):
    grid.append(list(map(int, r().split())))

for i in range (5):
    for x in range (10-(5-i)+1):
        for y in range (10-(5-i)+1):
            if grid[x][y]==0: continue
            breakFlag=False
            for bx in range (x, x+(5-i)):
                for by in range (y, y+(5-i)):
                    if grid[bx][by]!=1:
                        breakFlag=True
                        break
                if breakFlag==True: break
            
            if breakFlag==False:
                for bx in range (x, x+(5-i)):
                    for by in range (y, y+(5-i)):
                        grid[bx][by]=0 
                cnt[4-i]-=1
                total_cnt+=1
                
            if cnt[4-i]<0:
                exitFlag=True
                break
        if exitFlag==True: break
    if exitFlag==True: break
    
print(total_cnt if exitFlag==False else -1)