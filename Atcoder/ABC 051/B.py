K, S = [int(i) for i in input().split()]
t = 0
for a in range(K+1):
    for b in range(a, K+1):
        c = S - a - b
        if 0 <= c <= K and c >= a and c >= b:
            if a == b == c:
                t += 1
            elif a == b or b == c:
                t += 3
            else:
                t += 6
print(t)