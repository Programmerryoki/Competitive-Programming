S,T = [int(i) for i in input().split()]
count = 0
for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a + b + c > S:
                break
            if a*b*c <= T:
                count += 1
print(count)