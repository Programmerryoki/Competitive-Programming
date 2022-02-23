N = int(input())
ans = 0
for i in range(1, int(N**0.5) + 1):
    left = N // i
    for j in range(i, int(left ** 0.5) + 1):
        tmp = left // j
        if tmp < j:
            break
        ans += tmp - j + 1
print(ans)