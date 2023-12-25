N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    i,j,k = map(int,input().split())
    for shoot in range(i-1,j):
        baskets[shoot] = k

print(*baskets)
