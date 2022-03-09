import math

a=input()
l=[]
num_of_set_v1=0
num_of_set_v2=0
cnt=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (0, len(a)):
    cnt[int(a[i])]+=1

for i in range (0, len(cnt)):
    if i==6 or i==9:
        continue
    elif num_of_set_v1<cnt[i]:
        num_of_set_v1=cnt[i]
        
num_of_set_v2=math.ceil((cnt[6]+cnt[9])/2)        
if num_of_set_v1>num_of_set_v2: print(num_of_set_v1)
else: print(num_of_set_v2)