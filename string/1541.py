import sys

input = sys.stdin.readline

form = input().rstrip()
numbers = []
calculations = []

num = 0
for word in form:
    if '0'<=word<='9':
        num = 10 * num + int(word)
    else:
        numbers.append(num)
        calculations.append(word)
        num = 0
numbers.append(num)
        
idx = 0
while idx<len(calculations):
    if calculations[idx]=='+':
        new_number = numbers[idx] + numbers[idx+1]
        numbers = numbers[:idx] + [new_number] + numbers[idx+2:]
        calculations = calculations[:idx] + calculations[idx+1:]      
    else: idx += 1
    
result = numbers[0]
for i in range(len(calculations)):
    if calculations[i]=='-': result -= numbers[i+1]
    else: result += numbers[i+1]
    
print(result)
        