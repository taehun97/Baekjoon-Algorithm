num=int(input())
star_string=""

for i in range(num):
    for j in range (num-i):
        star_string+="*"
    print(star_string)
    star_string=""
