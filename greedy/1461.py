import sys

input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
pos_location = []
neg_location = []
for book in books:
    if book>0: pos_location.append(book)
    else: neg_location.append(-book)
    
pos_location.sort(reverse=True)
neg_location.sort(reverse=True)

answer = 0
if pos_location and neg_location:
    if pos_location[0]>neg_location[0]:
        for i in range(0, len(neg_location), M):
            answer += neg_location[i] * 2
        for i in range(0, len(pos_location), M):
            if i==0: answer += pos_location[i]
            else: answer += pos_location[i] * 2
    else:
        for i in range(0, len(pos_location), M):
            answer += pos_location[i] * 2
        for i in range(0, len(neg_location), M):
            if i==0: answer += neg_location[i]
            else: answer += neg_location[i] * 2
elif not pos_location:
    for i in range(0, len(neg_location), M):
        if i==0: answer += neg_location[i]
        else: answer += neg_location[i] * 2
elif not neg_location:
    for i in range(0, len(pos_location), M):
        if i==0: answer += pos_location[i]
        else: answer += pos_location[i] * 2

print(answer) 