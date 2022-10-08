import sys

input = sys.stdin.readline

string = list(input().rstrip())
str_len = len(string)

for i in range(0, str_len-1):
    end = i + 1
    if string[i]>string[end] and string[end]<=string[0]:
        string = list(reversed(string[:i+1])) + string[i+1:]
        if string[i]>=string[end]:
            string = list(reversed(string[:end+1])) + string[end+1:]
            
for e in string:
    print(e, end='')