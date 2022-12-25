import sys

input = sys.stdin.readline

end = int(input())
start = 1
point = 1
ans = [0 for _ in range(10)]

def cal(e, a, p):
    while e>0:
        a[e % 10] += p
        e //= 10

while start<=end:
    while end%10!=9:
        cal(end, ans, point)
        end -= 1
        
    if end<start: break
    
    while start%10!=0:
        cal(start, ans, point)
        start += 1
        
    start //= 10
    end //= 10
    
    for i in range(10):
        ans[i] += (end - start + 1) * point
    point *= 10
    
print(*ans)