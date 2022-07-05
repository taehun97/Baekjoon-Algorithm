import sys
read = sys.stdin.readline

str1 = str(read().strip())
str2 = str(read().strip())

temp = [0 for _ in range(len(str1))]

for i in range(len(str2)):
    cnt = 0
    for j in range(len(str1)):
        if cnt<temp[j]:
            cnt=temp[j]
        elif str1[j]==str2[i]:
            temp[j]=cnt+1
            
print(max(temp))