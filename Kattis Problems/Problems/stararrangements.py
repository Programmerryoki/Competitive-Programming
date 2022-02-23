S = int(input())
pos = []
for a in range(2, S+1):
    if (S)%(a) == 0 or S%a == (a//2 + a%2):
        pos.append([a//2 + a%2, a//2, a])

print(str(S)+":")
for a in pos:
    if a[0] != 1 or a[1] != 1:
        print(str(a[0]) + "," + str(a[1]))