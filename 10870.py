fibonacci=[0, 1];
input=int(input());

if(input==0 or input==1):
    print(fibonacci[input]);
else:   
    for i in range (2, input+1):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1]);
    print(fibonacci[input]);
