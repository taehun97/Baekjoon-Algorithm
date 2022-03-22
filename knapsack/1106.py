# from sys import stdin, maxsize

# r=stdin.readline

# # C는 유치해야 하는 고객의 수, N은 도시의 수를 의미함
# city=[[0, 0]]
# C, N=map(int, r().split())
# table=[0]+[maxsize for _ in range (C+100)]

# for _ in range (N):
#     m, p=map(int, r().split())
#     city.append([m, p])  

# for money, people in city:
#     for i in range (people, C+101):
#         table[i]=min(table[i], money+table[i-people])
        
# print(min(table[C:C+101]))

# ----------------------------------------------------------------------------

from sys import stdin, maxsize

r=stdin.readline

city=[[0, 0]]
C, N=map(int, r().split())
# table=[[0 if i==0 else maxsize for i in range (C+101)] for _ in range (N)]
table=[]

for i in range (N+1):
    temp=[]
    for j in range (C+101):
        if j==0: temp.append(0)
        else: temp.append(maxsize)
    table.append(temp)

for _ in range (N):
    m, p=map(int, r().split())
    city.append([m, p])  

for i in range (1, N+1):
    for j in range (city[i][1], C+101):
        if j-city[i][0]>=0:
            # print(table[i-1][j])
            # print(city[i][1])
            # print(table[i-1][j-city[i][0]])
            table[i][j]=min(table[i-1][j], city[i][1]+table[i-1][j-city[i][0]])
        else: table[i][j]=table[i-1][j]
    print()

print(min(table[N][C:C+101]))