# ---------------------------------------------------------------
# This is the code that I write after seeing the answer

import sys

r=sys.stdin.readline

N=int(r())
words=[]
digits=[]
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 
                 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

for _ in range(N):
    temp_list=list(r())
    temp_list.remove(temp_list[-1])
    words.append(temp_list)

for i in range (N):
    for j in range (len(words[i])):
        alphabet_dict[words[i][j]]+=10**(len(words[i])-1-j)
        
values=alphabet_dict.values()
for value in values:
    if value!=0:
        digits.append(value)

digits.sort(reverse=True)

d=9
sum=0
for i in range (len(digits)):
    sum+=(9-i)*digits[i]
    
print(sum)

# ---------------------------------------------------------------
# This is the code that I tried myself

# import sys
# import operator

# r=sys.stdin.readline
# N=int(r())
# words=[]
# alphabet_priority_pair={}
# alphabet=[]
# converted_words=[]

# for _ in range(N):
#     temp_list=list(r())
#     temp_list.remove(temp_list[-1])
#     words.append(temp_list)
    
# words.sort(key=len, reverse=True)

# for i in range (N):
#     for j in range (len(words[i])):
#         if words[i][j] not in alphabet:
#             alphabet_priority_pair.update({words[i][j]: [len(words[i])-j]})
#             alphabet.append(words[i][j])
#         else:
#             alphabet_priority_pair[words[i][j]].append(len(words[i])-j)
# alphabet_priority_pair=dict(sorted(alphabet_priority_pair.items(), key=operator.itemgetter(1), reverse=True))

# digits=list(alphabet_priority_pair.values())

# print(alphabet_priority_pair)


# num=9
# sum=0
# for i in range (len(digits)):
#     for j in range (len(digits[i])):
#         sum+=(num)*10**(digits[i][j]-1)
#     num-=1
#     print(sum)

# print(sum)
