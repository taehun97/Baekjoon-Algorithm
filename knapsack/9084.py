import sys

r=sys.stdin.readline

T=int(r())
cnt=0

def recursive_search(no, num_of_coin, values, total_cost):
    global cnt
    if num_of_coin==1:
        if total_cost%values[-1-no]==0: cnt+=1
    else:
        c_value=values[-1-no]
        quotient=total_cost//c_value
        for i in range (0, quotient+1):
            recursive_search(no+1, num_of_coin-1, values, total_cost-i*c_value)
        

for _ in range (T):
    N=int(r())
    coin_value=[0]+list(map(int, r().split())) # already sorted ascending
    M=int(r())
    
    recursive_search(0, N, coin_value, M)
    print(cnt)
    cnt=0