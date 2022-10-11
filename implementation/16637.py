from itertools import combinations

N = int(input())
expression = list(input().rstrip())
for i in range(0, len(expression), 2):
    expression[i] = int(expression[i])
answer = -float('inf')

def isPossible(combination):
    for i in range(len(combination)-1):
        if combination[i]==combination[i+1]-2: return False
        
    return True

def calculateBracket(exp, combination):
    returnExp = []
    result_list = []

    for c in combination:
        operand1 = exp[c]
        operator = exp[c+1]
        operand2 = exp[c+2]
        result = calculateExpression(operand1, operator, operand2)
        result_list.append(result)
        
    for i in range(len(result_list)):
        if i==0:
            returnExp += exp[0:combination[i]] + [result_list[i]]
        else: returnExp += exp[combination[i-1]+3:combination[i]] + [result_list[i]]
    
    if len(exp)-3>=combination[-1]:
        returnExp += exp[combination[-1]+3:]
    
    return returnExp

def calculate(exp):
    while len(exp)>1:
        operand1 = exp[0]
        operator = exp[1]
        operand2 = exp[2]
        result = calculateExpression(operand1, operator, operand2)
        exp = [result] + exp[3:]
        
    return exp[0]    

def calculateExpression(a, op, b):
    if op=='+': return a + b
    elif op=='-': return a - b
    elif op=='*': return a * b

if len(expression)==1:
    print(expression[0])
    exit()
    
element = [i * 2 for i in range(N//2)]
comb_list = []
for i in range(0, N//2):
    for c in combinations(element, i):
        comb_list.append(c)

for comb in comb_list:
    temp_expression = expression
    if isPossible(comb):
        if len(comb)!=0: temp_expression = calculateBracket(expression, list(comb))
        result = calculate(temp_expression)
        answer = max(answer, result)
        
print(answer)