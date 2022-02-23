N = int(input())
val = list(map(int, input()))
for a in range(N-1):
    print(val)
    temp = val[1]
    for b in range(N-a):
        val[b] = abs(val[b] - val[b+1])
print(val[0])