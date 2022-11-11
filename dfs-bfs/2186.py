import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

word = list(input().rstrip())
word_len = len(word)

dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(word_len)]

for w in range(word_len-1, -1, -1):
    search_alphabet = word[w]
    
    for i in range(N):
        for j in range(M):
            if board[i][j]==search_alphabet:
                if w==word_len - 1:
                    dp[w][i][j] = 1
                else:
                    for k in range(1, K+1):
                        for d in range(4):
                            nx, ny = i + dx[d] * k, j + dy[d] * k
                            if 0<=nx<N and 0<=ny<M and board[nx][ny]==word[w+1]:
                                dp[w][i][j] += dp[w+1][nx][ny]

print(sum(sum(dp[0][k]) for k in range(N)))