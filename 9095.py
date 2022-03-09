def dynamic(k):
    if k>3:
        d[k]=d[k-1] + d[k-2] + d[k-3]
    elif k==3:
        d[k]=d[k-1] + d[k-2] + 1
    elif k==2:
        d[k]=d[k-1] + 1
    else:
        d[k]=1

n=int(input())
ans=[]
temp=[0]*n
max_cur=0

for i in range (n):
    temp[i]=int(input())

m=max(temp)
d=[0 for col in range(m+1)]
max_cur=temp[0]

for i in range (n):
    if max_cur<=temp[i]:
        for j in range (1, temp[i]+1):
            if d[j]!=0 and i!=0:
                continue
            dynamic(j)
    print(d[temp[i]])