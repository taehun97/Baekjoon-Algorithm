from sys import stdin, maxsize

r=stdin.readline

# C는 유치해야 하는 고객의 수, N은 도시의 수를 의미함
city=[[0, 0]]
C, N=map(int, r().split())
table=[0]+[maxsize for _ in range (C+100)]

for _ in range (N):
    m, p=map(int, r().split())
    city.append([m, p])  

for money, people in city:
    for i in range (people, C+101):
        table[i]=min(table[i], money+table[i-people])

print(min(table[C:C+101]))