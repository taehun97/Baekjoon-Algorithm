import sys

input = sys.stdin.readline

n, l = map(int, input().split())
m_locations = [list(map(int, input().split())) for _ in range(n)]
answer = 0

m_locations.sort()

plank = m_locations[0][0]

for start, end in m_locations:
    if plank>end: # out of range
        continue
    elif plank<start: # out of range
        plank = start

    distance = end - plank
    
    count = distance // l + (0 if distance%l==0 else 1)
    plank += l * count
    answer += count
    
print(answer)
    