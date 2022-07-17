import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
table = [0]
answer = set()

def dfs(first, second, num):
    first.add(num)
    second.add(table[num])
    
    if table[num] in first:
        if first==second:
            answer.update(first)
            return True
        else: return False   
    return dfs(first, second, table[num])

for _ in range(n):
    table.append(int(input()))
    
for i in range(1, n+1):
    if i not in answer:
        dfs(set(), set(), i)
        
        
print(len(answer))
print(*sorted(list(answer)), sep='\n')