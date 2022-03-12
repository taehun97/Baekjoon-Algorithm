k=int(input())
a=[0] * (k+1)

def dynamic(n):
    a[n]=a[n-1]+1
    
    if n%3==0:
        a[n]=min(1+a[n//3], a[n])
        
    if n%2==0:
        a[n]=min(1+a[n//2], a[n])
  
for x in range (2, k+1):
    dynamic(x)
print(a[k])
     