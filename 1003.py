fibonacci_0=[1, 0, 1]
fibonacci_1=[0, 1, 1]
num=[]

input_num=int(input())

for i in range (0, input_num):
    num.append(int(input()));

for i in range (0, len(num)):
    length=len(fibonacci_0);
    if num[i]==1 or num[i]==0 or num[i]==2:
        print("%d %d"%(fibonacci_0[num[i]], fibonacci_1[num[i]]));
    else:
        for j in range (length, num[i]+1):
            fibonacci_0.append(fibonacci_0[j-1]+fibonacci_0[j-2]);
            fibonacci_1.append(fibonacci_1[j-1]+fibonacci_1[j-2]);
        print("%d %d"%(fibonacci_0[num[i]], fibonacci_1[num[i]]));