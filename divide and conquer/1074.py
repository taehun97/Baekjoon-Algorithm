import sys

r=sys.stdin.readline

N, r, c=map(int, r().split())
arr_size=(2**N)**2
length=2**N
result=0
standard_r=0
standard_c=0

while arr_size!=1:
    reduced_arr_size=int(arr_size/4)
    if r<standard_r+length/2 and c<standard_c+length/2: # 1사분면
        result+=reduced_arr_size*0
    elif r<standard_r+length/2 and c>=standard_c+length/2: # 2사분면
        standard_c+=length/2
        result+=reduced_arr_size*1
    elif r>=standard_r+length/2 and c<standard_c+length/2: # 3사분면
        standard_r+=length/2
        result+=reduced_arr_size*2
    else: # 4사분면
        standard_r+=length/2
        standard_c+=length/2
        result+=reduced_arr_size*3
    arr_size/=4
    length/=2

print(result)