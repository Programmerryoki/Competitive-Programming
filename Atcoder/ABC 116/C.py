N = int(input())
h = [int(i) for i in input().split()]
cur = [0]*N
water = 0
for i in range(N):
    while cur[i] < h[i]:
        water += 1
        j = i
        while j < N and cur[j] < h[j]:
            j += 1
        for k in range(i,j):
            cur[k] += 1
print(water)