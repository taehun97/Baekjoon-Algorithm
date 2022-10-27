import sys

input = sys.stdin.readline

n = int(input())

# 피사노 주기 풀이법
# n %= 1500000
# fib = [0, 1] + [0 for _ in range(n-1)]
# for i in range(2, n+1):
#     fib[i] = (fib[i-1] + fib[i-2])%1000000
    
# print(fib[n])

# 행렬 곱을 이용한 풀이법
if n<=2:
    print(1)
    exit()

def multiply2By2Matrix(b_matrix, r_matrix):
    returnMatrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result = 0
            for k in range(2):
                result += (b_matrix[i][k] * r_matrix[k][j]) % 1000000
            returnMatrix[i][j] = result % 1000000
    return returnMatrix

def fib(num):
    b_matrix = [[1, 1], [1, 0]]
    if num<=1: return b_matrix
    
    if num%2==0:
        half = fib(num//2)
        return multiply2By2Matrix(half, half)
    else:
        half = fib(num//2)
        twohalf = multiply2By2Matrix(half, half)
        return multiply2By2Matrix(twohalf, b_matrix)
            
result = fib(n-2)
print((result[0][0] + result[0][1]) % 1000000)