import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())
shark_infos = [list(map(int, input().split())) for _ in range(m)]
result = 0

def sharkMove():
    global r, c
    
    for i in range(len(shark_infos)):
        x = shark_infos[i][0]
        y = shark_infos[i][1]
        remaining_movement = shark_infos[i][2]
        d = shark_infos[i][3]
        
        while remaining_movement!=0:
            # print("hello")
            if d==1:
                if x-remaining_movement>=1:
                    x -= remaining_movement
                    remaining_movement = 0
                else:
                    remaining_movement -= (x - 1)
                    x = 1
                    d = 2
            elif d==2:
                if x+remaining_movement<=r:
                    x += remaining_movement
                    remaining_movement = 0
                else:
                    remaining_movement -= (r - x)
                    x = r
                    d = 1
            elif d==3:
                if y+remaining_movement<=c:
                    y += remaining_movement
                    remaining_movement = 0
                else:
                    remaining_movement -= (c - y)
                    y = c
                    d = 4    
            elif d==4:
                if y-remaining_movement>=1:
                    y -= remaining_movement
                    remaining_movement = 0
                else:
                    remaining_movement -= (y - 1)
                    y = 1
                    d = 3
                    
        shark_infos[i][0] = x
        shark_infos[i][1] = y
        shark_infos[i][3] = d
    
    cnt = 0
    info_cnt = len(shark_infos)
    while cnt<info_cnt:
        temp = []
        temp.append((shark_infos[cnt][4], cnt))
        
        cnt2 = cnt
        while cnt2<info_cnt:
            if shark_infos[cnt][0]==shark_infos[cnt2][0] and shark_infos[cnt][1]==shark_infos[cnt2][1]:
                temp.append((shark_infos[cnt2][4], cnt2))
            cnt2 += 1
        
        temp.sort()
        
        for i in range(len(temp)-1):
            print(shark_infos[temp[i][1]])
            shark_infos.remove(shark_infos[temp[i][1]])
            
        cnt += 1
        info_cnt -= (len(temp) - 1)
            
        

i = 0
while i<7:
    i += 1
    isFished = False
    fished_shark_idx = 0
    fished_shark_depth = float('inf')
    for n in range(len(shark_infos)):
        if shark_infos[n][1]==i:
            if shark_infos[n][0]<fished_shark_depth:
                isFished = True
                fished_shark_idx = n
                fished_shark_depth = shark_infos[n][0]
    
    if isFished:
        result += shark_infos[fished_shark_idx][4] 
        shark_infos.pop(fished_shark_idx)
    
    sharkMove()
    
print(result)