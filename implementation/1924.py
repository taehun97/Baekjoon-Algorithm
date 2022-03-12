date_array=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_sum=0

input_str=input()
month=int(input_str.split()[0])
date=int(input_str.split()[1])

for i in range (month-1):
    date_sum+=date_array[i]
date_sum+=date

day=date_sum%7

if day==1: print("MON")
elif day==2: print("TUE")
elif day==3: print("WED")
elif day==4: print("THU")
elif day==5: print("FRI")
elif day==6: print("SAT")
else: print("SUN")
