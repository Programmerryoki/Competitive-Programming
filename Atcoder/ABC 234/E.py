X = int(input())
sx = str(X)
mn = float("inf")
for i in range(int(sx[0]), 10):
    for j in range(-10, 10):
        n = str(i)
        s = i
        for _ in range(len(sx)-1):
            s += j
            if not (0 <= s < 10):
                break
            n += str(s)
        else:
            if int(n) >= X:
                mn = min(mn, int(n))
print(mn)