import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
sensor_info = [[sensor[0], 0]]
empty_space = []

chunk_cnt = 1
idx = 0
for i in range(1, N):
    if sensor[i]-sensor[i-1]<=1: continue
    else:
        empty_space.append(sensor[i]-sensor[i-1]-1)
        sensor_info[idx][1] = sensor[i-1]
        idx += 1
        sensor_info.append([sensor[i], 0])
        chunk_cnt += 1
sensor_info[-1][1] = sensor[-1]

empty_space.sort()

total_length = 0
for i in range(len(sensor_info)):
    total_length += sensor_info[i][1] - sensor_info[i][0]
    
for i in range(len(empty_space)):
    if chunk_cnt==K: break
    total_length += empty_space[i] + 1
    chunk_cnt -= 1
    
print(total_length)