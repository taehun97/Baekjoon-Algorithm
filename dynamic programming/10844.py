import copy

n = int(input())

temp = [0 for _ in range(10)]
temp2 = [0 for _ in range(10)]

for i in range(n):
    if i==0:
        for j in range(1, 10):
            temp[j]=1
    else:
        for j in range(10):
            if j==0: temp2[j+1]+=temp[j]
            elif j==9: temp2[j-1]+=temp[j]
            else:
                temp2[j+1]+=temp[j]
                temp2[j-1]+=temp[j]
                
        temp=copy.deepcopy(temp2)
        #temp2 = [0 for _ in range(10)]
        
print(sum(temp) % 1000000000)