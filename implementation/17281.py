import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
performance = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

def getScore(odr):
    idx = 0
    inning_idx = 0
    score = 0
    
    while inning_idx<N:
        idx, inning_score = inning(inning_idx, odr, idx)
        score += inning_score
        inning_idx += 1
        
    return score
        
def inning(inning_idx, odr, idx):
    b1, b2, b3 = 0, 0, 0
    score = 0
    outCount = 0
    
    while outCount<3:
        if performance[inning_idx][odr[idx]]==0:
            outCount += 1
        elif performance[inning_idx][odr[idx]]==1:
            score += b3
            b1, b2, b3 = 1, b1, b2
        elif performance[inning_idx][odr[idx]]==2:
            score += (b3 + b2)
            b1, b2, b3 = 0, 1, b1
        elif performance[inning_idx][odr[idx]]==3:
            score += (b3 + b2 + b1)
            b1, b2, b3 = 0, 0, 1
        elif performance[inning_idx][odr[idx]]==4:
            score += (b3 + b2 + b1 + 1)
            b1, b2, b3 = 0, 0, 0
                    
        idx = (idx + 1) % 9
    
    return idx, score

for p in permutations(range(1, 9), 8):
    order = list(p[:3]) + [0] + list(p[3:])
    max_score = max(max_score, getScore(order))
        
print(max_score)