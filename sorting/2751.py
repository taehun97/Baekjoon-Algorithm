import sys

r=sys.stdin.readline
array=[]

n=int(r())

for _ in range (n):
    array.append(int(r()))

array.sort()

for i in range (n):
    print(array[i])