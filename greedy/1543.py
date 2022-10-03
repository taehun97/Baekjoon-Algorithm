import sys

input = sys.stdin.readline

sentence = input().rstrip()
word = input().rstrip()
sentence_len = len(sentence)
word_len = len(word)

idx = 0
cnt = 0
while idx+word_len<=sentence_len:
    if sentence[idx:idx+word_len]==word:
        idx += word_len
        cnt += 1
    else:
        idx += 1

print(cnt)