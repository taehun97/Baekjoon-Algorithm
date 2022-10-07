from operator import neg
import sys

input = sys.stdin.readline

n = int(input())
neg_numbers = []
pos_numbers = []
isZero = False
for _ in range(n):
    number = int(input())
    if number>0: pos_numbers.append(number)
    elif number<0: neg_numbers.append(number)
    else: isZero = True
    
pos_numbers.sort(reverse = True)
neg_numbers.sort()

score = 0
neg_len = len(neg_numbers)
for i in range(0, neg_len, 2):
    if i!=neg_len-1: score += (neg_numbers[i] * neg_numbers[i+1])

if not isZero and neg_len%2==1: score += neg_numbers[-1]
    
pos_len = len(pos_numbers)        
for i in range(0, pos_len, 2):
    if i!=pos_len-1:
        if pos_numbers[i]==1 or pos_numbers[i+1]==1:
            score += (pos_numbers[i] + pos_numbers[i+1])
        else:
            score += (pos_numbers[i] * pos_numbers[i+1])
    else: score += pos_numbers[i]
        
print(score)