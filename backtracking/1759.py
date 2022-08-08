import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alphabet = list(input().split())

def backtracking(num, idx, candidate):
    if num==0:
        consonant = 0
        vowel = 0
        for element in candidate:
            if element in 'aeiou': consonant += 1
            else: vowel += 1
        
        if consonant>=1 and vowel>=2:    
            print(''.join(candidate))
        return
    
    for i in range(idx, c-num+1):
        candidate.append(alphabet[i])
        backtracking(num-1, i+1, candidate)
        candidate.pop()

alphabet.sort()

backtracking(l, 0, [])