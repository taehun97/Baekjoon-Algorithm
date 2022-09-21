import sys

input =sys.stdin.readline

L = int(input())
string = input().rstrip()
len_str = len(string)
lsp = [0 for _ in range(len_str)]

# LSP
j = 0
for i in range(1, len_str):
    while j>0 and string[i]!=string[j]:
        j = lsp[j-1]
    if string[i]==string[j]:
        j += 1
        lsp[i] = j
        
print(L - lsp[-1])