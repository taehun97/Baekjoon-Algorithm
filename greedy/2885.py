import sys

input = sys.stdin.readline

K = int(input())

min_chocolate = 1
while min_chocolate<K:
    min_chocolate = min_chocolate << 1
    
answer1 = min_chocolate
 
answer2 = 0
while K>0:
    if K>=min_chocolate:
        K -= min_chocolate # eat chocolate
    
    else:
        min_chocolate = min_chocolate >> 1 # cut chocolate
        answer2 += 1 # increment cut count
    
print(answer1, answer2)
       