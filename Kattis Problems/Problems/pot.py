n = int(input())
total = 0
for a in range(n):
    p = input()
    total += int(p[:-1])**int(p[-1])
print(total)