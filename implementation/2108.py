import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list=[]

for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)
    
num_list.sort()

average = round(sum(num_list)/N)

middle = num_list[N//2]

frequency = Counter(num_list).most_common()
frequent_num = frequency[0][0] if len(frequency)==1 or frequency[0][1]!=frequency[1][1] else frequency[1][0]

num_range = num_list[-1]-num_list[0]

print(average)
print(middle)
print(frequent_num)
print(num_range)