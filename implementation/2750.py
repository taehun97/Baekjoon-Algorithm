input_num=int(input())
unsort_array=[]

for i in range (input_num):
    num=int(input())
    unsort_array.append(num)

unsort_array.sort()

for i in range(input_num):
    print(unsort_array[i])