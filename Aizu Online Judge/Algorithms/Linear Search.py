n = int(input())
s = input().split()
q = int(input())
T = input().split()
c = 0
for a in T:
    if a in s:
        c += 1
print(c)