import sys

input = sys.stdin.readline

string = input().rstrip()
str_len = len(string)
front, back = 0, 1
max_len = 0

while front!=str_len or back!=str_len:
    if front==back:
        back += 1
    
    if string[front:back] in string[front+1:]:
        max_len = max(max_len, len(string[front:back]))
        back += 1
    else: front += 1
    
print(max_len)