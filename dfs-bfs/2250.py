import sys

input = sys.stdin.readline

n = int(input())
node_info = [[-1, -1] for _ in range(n+1)]
node = [0 for _ in range(n+1)]
r = [[] for _ in range(n+1)]
root = 0
num = 0

def inorder(root, level):
    global num
    
    if node_info[root][0]!=-1:
        inorder(node_info[root][0], level+1)
        
    num += 1
    r[level].append(num)
    
    if node_info[root][1]!=-1:
        inorder(node_info[root][1], level+1)
        
for _ in range(n):
    m, x, y = map(int, input().split())
    node_info[m][0] = x
    node_info[m][1] = y
    
    node[m]+=1
    if x!=-1: node[x]+=1
    if y!=-1: node[y]+=1

for i in range(1, n+1):
    if node[i]==1: root = i
        
inorder(root, 1)

result_depth = 1
result_breadth = max(r[1]) - min(r[1]) + 1

for i in range(2, n+1):
    if r[i]:
        if result_breadth<max(r[i])-min(r[i])+1:
            result_breadth = max(r[i]) - min(r[i]) + 1
            result_depth = i
            
print(result_depth, result_breadth)