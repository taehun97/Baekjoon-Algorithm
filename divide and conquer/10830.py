import sys
    
def multiply_matrix(a, b):
    temp=[]
    for i in range (n):
        temp_row=[]
        for j in range (n):
            sum=0
            for k in range (n):
                sum+=a[i][k]*b[k][j]
            temp_row.append(sum%1000)
        temp.append(temp_row)
    return temp

r=sys.stdin.readline

n, b=tuple(map(int, r().split()))
matrix=[]
elementary_matrix=[]
result=[]

for _ in range (n):
    temp=list(map(int, r().split()))
    matrix.append(temp)

for i in range (n):
    temp=[]
    for j in range (n):
        if i==j: 
            temp.append(1)
        else: 
            temp.append(0)
    elementary_matrix.append(temp)
    result.append(temp)
    

num=bin(b)[2:]
for i in range (len(num)):
    if num[-i-1]=='1':
        i_temp=i
        temp=matrix
        while i_temp>0:
            temp=multiply_matrix(temp, temp)
            i_temp-=1
        result=multiply_matrix(temp, result)

for i in range (n):
    for j in range (n):
        print(result[i][j], end=' ')
    print()