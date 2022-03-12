result=0
is_visited=[False]*10000

for i in range (1, 10000):
    result=i
    while result<10000:
        result=result+(result%10)+(int(result/10)%10)+(int(result/100)%10)+(int(result/1000)%10)
        if result<10000: is_visited[result]=True

for i in range (1, 10000):
    if is_visited[i]==False: print(i)      