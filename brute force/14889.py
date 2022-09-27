import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
human_id = [i for i in range(N)]

human_combs = list(combinations(human_id, N//2))
answer = float('inf')

for comb in human_combs:
    remain = tuple(set(human_id) - set(comb))

    start, link = 0, 0
    for i in range(N//2):
        for j in range(N//2):
            start += board[comb[i]][comb[j]]
            link += board[remain[i]][remain[j]]
    
    answer = min(answer, abs(start-link))
    
print(answer)
