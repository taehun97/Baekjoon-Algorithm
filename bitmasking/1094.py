import sys

input = sys.stdin.readline

X = int(input())

string = bin(X)[2:]
converted_string = list(map(int, list(string)))

print(sum(converted_string))