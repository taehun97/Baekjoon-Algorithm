from re import T
import sys

r=sys.stdin.readline

num=int(r())
positive=[]
zero=[]
negative=[]
max=0

for _ in range (num):
    element=int(r())
    if element>0:
        positive.append(element)
    elif element<0:
        negative.append(element)
    else:
        zero.append(element)

positive.sort()
negative.sort(reverse=True)

for _ in range (0, len(positive)//2):
    num1=positive.pop()
    num2=positive.pop()
    if num1==1 or num2==1:
        max+=num1+num2
    else:
        max+=num1*num2
if len(positive)%2!=0:
    max+=positive.pop()


for _ in range (0, len(negative)//2):
    num1=negative.pop()
    num2=negative.pop()
    max+=num1*num2
if len(negative)%2!=0:
    if len(zero)==1:
        max+=negative.pop()*zero[0]
    elif len(zero)==0:
        max+=negative.pop()

print(max)