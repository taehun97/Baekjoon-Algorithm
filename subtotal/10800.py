from sys import stdin


def return_size(ball):
    return ball[2]


n = int(stdin.readline())

balls = []
for i in range(n):
    c, s = map(int, stdin.readline().split())
    balls.append([i, c, s])

balls.sort(key=return_size)

s = 0
j = 0
color = [0] * (n + 1)
answer = [0] * n
for i in range(n):
    a = balls[i]
    b = balls[j]

    while b[2] < a[2]:
        s += b[2]
        color[b[1]] += b[2]
        j += 1
        b = balls[j]

    answer[a[0]] = s - color[a[1]]

print("\n".join(map(str, answer)))