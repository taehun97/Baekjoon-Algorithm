matrix = [input() for _ in range(5)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result_set = set()


def backtrack(arr, index=0, S=0, Y=0):
    tmp = arr
    if Y > 3:
        return
    if index == 6:
        arr.sort()
        result_set.add(tuple(arr))
    else:
        adjacents = []
        for node in range(len(arr)):
            for i in range(4):
                dx = arr[node][0] + delta[i][0]
                dy = arr[node][1] + delta[i][1]
                if 0 > dx or 5 <= dx or 0 > dy or 5 <= dy: continue
                if (dx, dy) in arr: continue
                adjacents.append((dx,dy))
        for adjacent in adjacents:
            nx = adjacent[0]
            ny = adjacent[1]
            if matrix[nx][ny] == 'S':
                backtrack(arr+[(nx,ny)], index+1, S+1, Y)
            else:
                backtrack(arr+[(nx,ny)], index+1, S, Y+1)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'S':
            backtrack([(i, j)], index=0, S=1)

print(len(result_set))