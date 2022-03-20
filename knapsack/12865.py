import sys

r=sys.stdin.readline

store=[]
N, K=map(int, r().split())
arr=[[0]*(K+1) for _ in range (N+1)]

for _ in range (N):
    m, v=map(int, r().split())
    store.append([m, v])

def knapsack(num_of_thing, s, limit):
    for i in range (1, num_of_thing+1):
        for j in range (1, limit+1):
            if j>=s[i-1][0]:
                arr[i][j]=max(s[i-1][1]+arr[i-1][j-s[i-1][0]], arr[i-1][j])
            else:
                arr[i][j]=arr[i-1][j]

knapsack(N, store, K)
print(arr[N][K])