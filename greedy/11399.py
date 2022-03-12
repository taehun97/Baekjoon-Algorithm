num=int(input())
time_spent=list(map(int, input().split()))
total=0

time_spent.sort()
for i in range (num):
    # total+=(num-i)*time_spent[i]
    # or
    total+=sum(time_spent[:i+1])

print(total)