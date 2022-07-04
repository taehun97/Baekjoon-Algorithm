N = int(input())

def moo(total, middle, index):
    prevTotal=(total-middle)//2
    if index<=prevTotal: return moo(prevTotal, middle-1, index)
    elif index>prevTotal+middle: return moo(prevTotal, middle-1, index-prevTotal-middle)
    else: return "m" if index==prevTotal+1 else "o"

k=3
sum=3

while sum<N:
    k+=1
    sum=sum*2+k
    
print(moo(sum, k, N))