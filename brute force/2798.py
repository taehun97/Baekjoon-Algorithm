import sys

r=sys.stdin.readline

n, m=tuple(map(int, r().split()))
card=list(map(int, r().split()))
card.sort()
sum_of_card=card[0]+card[1]+card[2]
diff=m-sum_of_card

for i in range (n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            new_diff=m-(card[i]+card[j]+card[k])
            if new_diff<diff and new_diff>=0:
                sum_of_card=card[i]+card[j]+card[k]
                diff=m-sum_of_card
                
print(sum_of_card)