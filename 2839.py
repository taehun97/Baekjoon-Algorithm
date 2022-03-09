total_sugar=int(input())

if total_sugar%5==0:
    print(int(total_sugar/5))
else:
    if((total_sugar%5)%3==0): print(int(total_sugar/5)+int((total_sugar%5)/3))
    else:
        sum=total_sugar%5;
        if int(total_sugar/5)==0: print(-1)
        else:
            for i in range (0, int(total_sugar/5)):
                sum+=5
                if sum%3==0:
                    print(int(total_sugar/5)-(i+1)+int(sum/3))
                    break
                else:
                    if i+1==int(total_sugar/5): print(-1)