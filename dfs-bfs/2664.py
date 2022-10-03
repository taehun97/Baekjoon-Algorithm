import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
parents = [-1 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    parents[y] = x
    
ancestor_a_list = []
ancestor_pointer = a
degree_a = 0
while ancestor_pointer!=-1:
    ancestor_a_list.append((ancestor_pointer, degree_a))
    ancestor_pointer = parents[ancestor_pointer]
    degree_a += 1
    
ancestor_b_list = []
ancestor_pointer = b
degree_b = 0
while ancestor_pointer!=-1:
    ancestor_b_list.append((ancestor_pointer, degree_b))
    ancestor_pointer = parents[ancestor_pointer]
    degree_b += 1
    
answer = -1
for ancestor_a, da in ancestor_a_list:
    for ancestor_b, db in ancestor_b_list:
        if ancestor_a==ancestor_b:
            answer = da + db
            print(answer)
            exit()
            
print(answer)