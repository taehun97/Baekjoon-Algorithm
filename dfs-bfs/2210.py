from collections import deque

direction_x=[1, -1, 0, 0]
direction_y=[0, 0, 1, -1]

queue=deque()
array=[[0]*5 for i in range (5)]
num_str=""
num_str_list=[]
str_len=1;
is_str_len_count=False

def dfs(x, y):
    global str_len, is_str_len_count, num_str

    queue.append((x, y))
    while queue:
        qx, qy=queue.pop()
        for i in range(4):
            nx=qx+direction_x[i]
            ny=qy+direction_y[i]
            if 0<=nx<len(array) and 0<=ny<len(array[0]):
                if str_len<6:
                    print(queue)
                    queue.append((nx, ny))
                    print(queue)
                    if is_str_len_count==False:
                        str_len+=1
                        num_str+=str(array[nx][ny])
                    is_str_len_count=True
                elif str_len==6:
                    for j in range (len(num_str_list)):
                        if num_str_list[j]==num_str:
                            break
                        else:
                            if j==len(num_str_list)-1:
                                num_str_list.append(num_str)
                    str_len-=1
                    num_str=num_str[:-1]
                    break

        is_str_len_count=False
                

for i in range (len(array)):
    ary_element=input().split(' ')
    for j in range (len(array[i])):
        array[i][j]=int(ary_element[j])

for i in range (len(array)):
    for j in range (len(array[i])):
        dfs(i, j)

print(len(num_str_list))