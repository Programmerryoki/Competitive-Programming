N = int(input())
H = [int(i) for i in input().split()]
m = 0
c = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)